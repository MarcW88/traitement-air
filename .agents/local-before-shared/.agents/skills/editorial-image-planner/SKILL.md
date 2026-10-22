---
name: editorial-image-planner
description: Decide whether a Thuisrenovatie Gids page genuinely benefits from an editorial image, then create a safe BFL/FLUX request. Use after content is written and before publication.
license: MIT
metadata:
  adapted_for: thuisrenovatie-gids.nl
  generator: Black Forest Labs FLUX API
  default_model: FLUX.2 Pro Preview
---

# Editorial Image Planner — Thuisrenovatie Gids

## Goal

Add images only when they improve understanding, orientation or editorial rhythm. Generated imagery is contextual illustration, never proof of a real installation, inspection, quote, product test or technical result.

Generation is driven by `.content/image-requests/*.json`. The engine only generates requests with `required: true`, `allow_ai_generation: true`, `truth_risk: LOW` and status `PENDING` or `REGENERATE`.

## When an image is useful

Generate an image when it clearly helps a reader picture a renovation context, a room or building situation, a planning/decision moment, a non-branded work environment, or a problem that is easier to recognize visually than through text alone.

Default to 0 or 1 generated image per page. A second image needs a distinct editorial role.

## Do not generate

Use `allow_ai_generation: false` or `BLOCKED` when visual fidelity is essential, including exact branded products, logos, electrical or refrigerant wiring details, regulatory diagrams, structural defects requiring professional diagnosis, precise construction assemblies, measurements, charts, screenshots, invoices, legal documents or anything presented as evidence from a real inspection.

For technical renovation pages, keep generated images contextual rather than instructional: show the setting, not a potentially unsafe step-by-step procedure.

## Preferred visual direction

Images should match the site's architectural, warm and premium-accessible identity:

- contemporary Dutch/Benelux residential context;
- natural daylight and believable materials;
- candid editorial photography rather than advertising imagery;
- warm neutral interiors, mineral/wood/brick textures where appropriate;
- realistic imperfections and lived-in context;
- no visible logos, watermarks or readable invented text;
- no exaggerated before/after effect;
- no fake certificates, badges or trust signals.

Avoid generic eco stock-photo clichés, hyper-saturated green imagery, glossy catalogue staging and futuristic architecture.

## Request format

Copy `.content/image-requests/_template.json` to `.content/image-requests/<slug>-<slot>.json` and set:

- `page`: generated HTML page, e.g. `verduurzamen/isolatie/index.html`;
- `required`: editorial decision;
- `reason`: why the image helps;
- `allow_ai_generation`: truth/safety gate;
- `truth_risk`: `LOW` for automated generation;
- `status`: `PENDING`, `BLOCKED`, `NOT_NEEDED`, `GENERATED` or `REGENERATE`;
- `marker`: unique HTML comment also present in `content/<route>/body.html`;
- `output_path`: under `assets/generated/`;
- `prompt`: complete photographic brief;
- `alt`: useful concise Dutch alt text;
- `width`, `height`, `prompt_upsampling`, optional `seed`.

Default FLUX.2 Pro Preview dimensions are 1024×672 with prompt upsampling enabled.

## Marker rule

The marker must be in the source body that regenerates the page, not only in generated HTML.

Example:

```html
<!-- EDITORIAL_IMAGE:isolatie-context -->
```

Place it where the visual adds value, preferably after an introductory explanation or immediately before the section it illustrates. The BFL workflow regenerates pages first, then replaces the marker in generated HTML with the `<figure>`. When the site is regenerated later, the marker returns and the existing image is reinserted without a new paid generation.

## Prompt pattern

Describe subject/action, residential setting, light, framing, relevant materials, photographic aesthetic and truth constraints. A useful ending is:

`photorealistic editorial photography, natural daylight, realistic Dutch residential proportions and materials, candid documentary framing, no visible brand, no readable text, no watermark, no staged advertising look`

## Publication gate

Before setting a request to `PENDING`, confirm that the image has a clear role, can be safely generic, does not pretend to document a real job or diagnosis, the marker exists in the source body, the output path is unique and the alt text describes the image rather than an SEO keyword target.
