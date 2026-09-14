#!/usr/bin/env python3
"""Generate approved editorial images with Black Forest Labs FLUX.

Requests live in .content/image-requests/*.json. Only requests that are explicitly
required, allowed for AI generation, LOW truth-risk and PENDING/REGENERATE are
sent to BFL. GENERATED requests can reinsert an existing image after site
regeneration without paying for a new generation.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_REQUESTS_DIR = ".content/image-requests"
DEFAULT_BFL_API_URL = "https://api.bfl.ai/v1/flux-2-pro-preview"
ACTIVE_STATUSES = {"PENDING", "REGENERATE"}
VALID_STATUSES = {"NOT_NEEDED", "BLOCKED", "PENDING", "GENERATED", "REGENERATE"}
VALID_PLACEMENTS = {"replace", "before", "after"}
TERMINAL_FAILURES = {"Error", "Failed"}


class RequestError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--requests-dir", default=DEFAULT_REQUESTS_DIR)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--github-output", default=None)
    parser.add_argument("--api-url", default=os.environ.get("BFL_API_URL", DEFAULT_BFL_API_URL))
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("BFL_TIMEOUT", "600")))
    parser.add_argument("--poll-interval", type=float, default=float(os.environ.get("BFL_POLL_INTERVAL", "1")))
    return parser.parse_args()


def request_files(root: Path, requests_dir: str) -> list[Path]:
    directory = root / requests_dir
    if not directory.exists():
        return []
    return sorted(path for path in directory.glob("*.json") if path.name != "_template.json")


def load_request(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RequestError(f"{path}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise RequestError(f"{path}: JSON root must be an object")
    return data


def safe_repo_path(root: Path, value: str, field: str, source: Path) -> Path:
    if not value or not isinstance(value, str):
        raise RequestError(f"{source}: missing field {field!r}")
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise RequestError(f"{source}: unsafe {field!r} path: {value}")
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise RequestError(f"{source}: {field!r} leaves repository root") from exc
    return resolved


def output_format_for(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".png":
        return "png"
    if suffix in {".jpg", ".jpeg"}:
        return "jpeg"
    if suffix == ".webp":
        return "webp"
    raise RequestError(f"Unsupported image extension: {suffix or '(none)'}")


def validate_request(root: Path, source: Path, req: dict[str, Any]) -> None:
    request_id = req.get("id")
    if not isinstance(request_id, str) or not request_id.strip():
        raise RequestError(f"{source}: missing id")

    status = req.get("status")
    if status not in VALID_STATUSES:
        raise RequestError(f"{source}: invalid status {status!r}")

    placement = req.get("placement", "replace")
    if placement not in VALID_PLACEMENTS:
        raise RequestError(f"{source}: invalid placement {placement!r}")

    required = req.get("required")
    allowed = req.get("allow_ai_generation")
    if not isinstance(required, bool) or not isinstance(allowed, bool):
        raise RequestError(f"{source}: required and allow_ai_generation must be booleans")

    if not required and status in ACTIVE_STATUSES:
        raise RequestError(f"{source}: non-required request cannot be {status}")

    if status in ACTIVE_STATUSES:
        if not allowed:
            raise RequestError(f"{source}: {status} requires allow_ai_generation=true")
        if req.get("truth_risk") != "LOW":
            raise RequestError(f"{source}: automatic generation requires truth_risk=LOW")

    if status in ACTIVE_STATUSES or status == "GENERATED":
        for field in ("page", "marker", "output_path", "prompt", "alt"):
            value = req.get(field)
            if not isinstance(value, str) or not value.strip():
                raise RequestError(f"{source}: field {field!r} is required")

        output_path = str(req["output_path"])
        if not output_path.startswith("assets/generated/"):
            raise RequestError(f"{source}: output_path must remain under assets/generated/")
        output_format_for(output_path)
        safe_repo_path(root, str(req["page"]), "page", source)
        safe_repo_path(root, output_path, "output_path", source)

        width = req.get("width")
        height = req.get("height")
        for field, value in (("width", width), ("height", height)):
            if not isinstance(value, int) or value < 64 or value > 2048 or value % 16:
                raise RequestError(f"{source}: {field} must be 64..2048 and a multiple of 16")
        if int(width) * int(height) > 4_194_304:
            raise RequestError(f"{source}: resolution exceeds 4MP")


def figure_markup(req: dict[str, Any]) -> str:
    request_id = html.escape(str(req["id"]), quote=True)
    src = "/" + str(req["output_path"]).lstrip("/")
    alt = html.escape(str(req["alt"]), quote=True)
    caption = str(req.get("caption") or "").strip()
    width = int(req["width"])
    height = int(req["height"])
    lines = [
        f'<figure class="editorial-media" data-generated-image="{request_id}">',
        f'  <img src="{html.escape(src, quote=True)}" alt="{alt}" width="{width}" height="{height}" loading="lazy" decoding="async">',
    ]
    if caption:
        lines.append(f"  <figcaption>{html.escape(caption)}</figcaption>")
    lines.append("</figure>")
    return "\n".join(lines)


def request_needs_generation(req: dict[str, Any]) -> bool:
    return bool(
        req.get("required")
        and req.get("allow_ai_generation")
        and req.get("truth_risk") == "LOW"
        and req.get("status") in ACTIVE_STATUSES
    )


def page_needs_insertion(root: Path, source: Path, req: dict[str, Any]) -> bool:
    if req.get("status") != "GENERATED":
        return False
    if not req.get("required") or not req.get("allow_ai_generation") or req.get("truth_risk") != "LOW":
        return False
    page_path = safe_repo_path(root, str(req["page"]), "page", source)
    output_path = safe_repo_path(root, str(req["output_path"]), "output_path", source)
    if not page_path.exists() or not output_path.exists():
        return False
    text = page_path.read_text(encoding="utf-8")
    marker = str(req["marker"])
    token = f'data-generated-image="{req["id"]}"'
    return marker in text and token not in text


def check_work(root: Path, sources: list[Path]) -> tuple[bool, int, int]:
    seen_outputs: dict[str, Path] = {}
    pending = 0
    reinsert = 0
    for source in sources:
        req = load_request(source)
        validate_request(root, source, req)
        output = str(req.get("output_path") or "")
        if output:
            previous = seen_outputs.get(output)
            if previous and previous != source:
                raise RequestError(f"{source}: duplicate output_path with {previous}: {output}")
            seen_outputs[output] = source
        if request_needs_generation(req):
            page_path = safe_repo_path(root, str(req["page"]), "page", source)
            if not page_path.exists():
                raise RequestError(f"{source}: target page missing: {req['page']}")
            page_text = page_path.read_text(encoding="utf-8")
            token = f'data-generated-image="{req["id"]}"'
            if str(req["marker"]) not in page_text and token not in page_text:
                raise RequestError(f"{source}: marker missing from generated page: {req['marker']}")
            pending += 1
        elif page_needs_insertion(root, source, req):
            reinsert += 1
    return (pending + reinsert > 0, pending, reinsert)


def json_request(url: str, api_key: str, *, payload: dict[str, Any] | None = None, timeout: int = 60) -> dict[str, Any]:
    headers = {"accept": "application/json", "x-key": api_key}
    data = None
    method = "GET"
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
        method = "POST"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RequestError(f"BFL HTTP {exc.code}: {detail[:1000]}") from exc
    except urllib.error.URLError as exc:
        raise RequestError(f"Unable to reach BFL API: {exc}") from exc
    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RequestError("BFL returned non-JSON response") from exc
    if not isinstance(parsed, dict):
        raise RequestError("Unexpected BFL response")
    return parsed


def download_binary(url: str, timeout: int = 120) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "thuisrenovatie-gids-image-bot/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = response.read()
    except urllib.error.URLError as exc:
        raise RequestError(f"Unable to download BFL image: {exc}") from exc
    if not data:
        raise RequestError("BFL returned an empty image")
    return data


def call_bfl(api_url: str, timeout: int, poll_interval: float, req: dict[str, Any]) -> tuple[bytes, dict[str, Any]]:
    api_key = os.environ.get("BFL_API_KEY", "").strip()
    if not api_key:
        raise RequestError("Secret BFL_API_KEY is missing")
    payload: dict[str, Any] = {
        "prompt": req["prompt"],
        "width": int(req["width"]),
        "height": int(req["height"]),
        "output_format": output_format_for(str(req["output_path"])),
        "prompt_upsampling": bool(req.get("prompt_upsampling", True)),
    }
    seed = req.get("seed")
    if isinstance(seed, int) and seed >= 0:
        payload["seed"] = seed
    submitted = json_request(api_url, api_key, payload=payload, timeout=min(timeout, 120))
    polling_url = submitted.get("polling_url")
    request_id = submitted.get("id")
    if not isinstance(polling_url, str) or not polling_url:
        raise RequestError(f"BFL did not return polling_url: {submitted!r}")
    deadline = time.monotonic() + timeout
    while True:
        if time.monotonic() >= deadline:
            raise RequestError(f"BFL timeout after {timeout}s (request id: {request_id})")
        time.sleep(max(0.5, poll_interval))
        result = json_request(polling_url, api_key, timeout=min(timeout, 120))
        status = result.get("status")
        print(f"BFL status {request_id}: {status}")
        if status == "Ready":
            result_data = result.get("result")
            sample = result_data.get("sample") if isinstance(result_data, dict) else None
            if not isinstance(sample, str) or not sample:
                raise RequestError(f"BFL Ready without result.sample: {result!r}")
            image = download_binary(sample)
            return image, {
                "bfl_request_id": request_id,
                "bfl_endpoint": api_url,
                "bfl_cost": submitted.get("cost"),
            }
        if status in TERMINAL_FAILURES:
            raise RequestError(f"BFL generation failed: {result!r}")


def insert_or_restore_figure(root: Path, source: Path, req: dict[str, Any]) -> bool:
    page_path = safe_repo_path(root, str(req["page"]), "page", source)
    output_path = safe_repo_path(root, str(req["output_path"]), "output_path", source)
    if not output_path.exists():
        raise RequestError(f"{source}: image missing: {req['output_path']}")
    if not page_path.exists():
        raise RequestError(f"{source}: target page missing: {req['page']}")
    text = page_path.read_text(encoding="utf-8")
    marker = str(req["marker"])
    token = f'data-generated-image="{req["id"]}"'
    if token in text:
        return False
    if marker not in text:
        raise RequestError(f"{source}: marker missing: {marker}")
    figure = figure_markup(req)
    placement = str(req.get("placement", "replace"))
    if placement == "before":
        replacement = f"{figure}\n\n{marker}"
    elif placement == "after":
        replacement = f"{marker}\n\n{figure}"
    else:
        replacement = figure
    page_path.write_text(text.replace(marker, replacement, 1), encoding="utf-8")
    return True


def write_request(path: Path, req: dict[str, Any]) -> None:
    path.write_text(json.dumps(req, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def process(root: Path, sources: list[Path], args: argparse.Namespace) -> None:
    for source in sources:
        req = load_request(source)
        validate_request(root, source, req)
        if request_needs_generation(req):
            page_path = safe_repo_path(root, str(req["page"]), "page", source)
            page_text = page_path.read_text(encoding="utf-8")
            token = f'data-generated-image="{req["id"]}"'
            if str(req["marker"]) not in page_text and token not in page_text:
                raise RequestError(f"{source}: marker missing from generated page")
            image, metadata = call_bfl(args.api_url, args.timeout, args.poll_interval, req)
            output_path = safe_repo_path(root, str(req["output_path"]), "output_path", source)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(image)
            req["status"] = "GENERATED"
            req["generated_at"] = datetime.now(timezone.utc).isoformat()
            req.update(metadata)
            write_request(source, req)
            insert_or_restore_figure(root, source, req)
            print(f"Generated {req['id']} -> {req['output_path']}")
        elif page_needs_insertion(root, source, req):
            if insert_or_restore_figure(root, source, req):
                print(f"Reinserted existing image for {req['id']}")


def write_github_output(path: str | None, work_needed: bool, pending: int, reinsert: int) -> None:
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(f"work_needed={'true' if work_needed else 'false'}\n")
        handle.write(f"pending_count={pending}\n")
        handle.write(f"reinsert_count={reinsert}\n")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    sources = request_files(root, args.requests_dir)
    try:
        work_needed, pending, reinsert = check_work(root, sources)
        print(f"Image requests: {len(sources)} | pending={pending} | reinsert={reinsert}")
        write_github_output(args.github_output, work_needed, pending, reinsert)
        if args.check_only:
            return 0
        if work_needed:
            process(root, sources, args)
        return 0
    except RequestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
