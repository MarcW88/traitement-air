# Post-write gap check — <route>

Workflow version: 2
Research artifact: <path to SERP coverage matrix>
Brief: <path to brief>
Draft/source: <path to body.html>
Review date: YYYY-MM-DD

## Coverage verification

Map every `MUST` and relevant `SHOULD` item from the pre-write matrix to the final page.

| Requirement | Priority | Final status | Where covered | Evidence/source preserved? | Notes |
|---|---|---|---|---|---|
| | MUST / SHOULD | COVERED / PARTIAL / MISSING | heading/paragraph | yes/no/n-a | |

## GEO verification

- Direct answers are present where natural: yes/no
- Important factual claims are atomic and source-adjacent: yes/no
- Volatile claims show relevant date/scope: yes/no
- No manufactured FAQ/snippet blocks added only for GEO: yes/no
- Useful original synthesis/information gain survives the style passes: yes/no

## Voice / anti-slop verification

- Brand voice applied: yes/no
- Humanizer run separately: yes/no
- General-writing pass run separately: yes/no
- Anti-ai-slop review run separately: yes/no
- Repeated cluster template introduced: yes/no

## Gate

Any unresolved `MUST = MISSING`, unsupported central claim, stale required evidence, or unresolved intent/cannibalisation issue forces:

`FAIL — KEEP_NOINDEX`

`PARTIAL` on a MUST item requires an explicit rationale; it cannot silently pass.
