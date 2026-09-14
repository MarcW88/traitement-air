# Design audit workflow

This directory is orchestration only. It does not define a custom design-scoring system.

The analysis engines are maintained in existing GitHub repositories and are installed as pinned npm dependencies. The local code chooses which Thuisrenovatie Gids routes to inspect, starts the static site, captures browser renders, and stores upstream tool output without replacing the upstream rules.

## Upstream analysis engines

### Impeccable — design quality and generic/AI-like frontend patterns

- Repository: `https://github.com/pbakaus/impeccable`
- Package: `impeccable@4.1.0`
- Role: deterministic design-quality scan of HTML/CSS/source files. The upstream CLI documents 61 detector rules covering generic/AI-like UI patterns, typography, color and contrast, layout/composition, motion and interface-quality problems.
- Local customization: none to the detector rules. The repository paths passed to `impeccable detect` are the only project-specific choice.

### Playwright — rendered browser verification and screenshots

- Repository: `https://github.com/microsoft/playwright`
- Package: `@playwright/test@1.63.0`
- Role: load the real static pages in Chromium, render desktop and mobile viewports, capture full-page screenshots, exercise the mobile navigation, and expose console/runtime failures.
- The local runner is adapted from the existing GitHub implementation in `MarcW88/bloc-notes-numerique/.agents/skills/site-design-review/scripts/run-visual-review.mjs`. Changes are limited to reading routes from this repository's sitemap, using this site's `.menu-toggle`, and attaching axe-core results.

### axe-core — accessibility in the rendered DOM

- Repository: `https://github.com/dequelabs/axe-core`
- Playwright integration package: `@axe-core/playwright@4.13.0`
- Role: accessibility rules against each rendered route and viewport.
- Local customization: no custom axe rules or exclusions.

### Lighthouse CI — rendered performance, accessibility and best practices

- Repository: `https://github.com/GoogleChrome/lighthouse-ci`
- Package: `@lhci/cli@0.15.1`
- Role: collect Lighthouse reports for every sitemap route, split by site scope in CI.
- Categories retained: performance, accessibility and best-practices. No custom scoring weights or pass/fail thresholds are introduced.

### html-validate — HTML structure and validity

- Repository: `https://github.com/html-validate/html-validate`
- Package: `html-validate@11.15.0`
- Role: validate generated HTML documents.
- Configuration: upstream `html-validate:recommended` only. No local rule overrides.

### Stylelint — CSS correctness and conventions

- Repository: `https://github.com/stylelint/stylelint`
- Standard config repository: `https://github.com/stylelint/stylelint-config-standard`
- Packages: `stylelint@17.15.0`, `stylelint-config-standard@40.0.0`
- Role: inspect the CSS implementation for invalid/problematic CSS and modern standard conventions.
- Configuration: upstream standard config only. No local rule overrides.

### ESLint — JavaScript correctness

- Repository: `https://github.com/eslint/eslint`
- Packages: `eslint@10.9.1`, `@eslint/js@10.0.1`
- Role: static analysis of the site's JavaScript.
- Configuration: upstream recommended rule set. The only project-specific setting declares `document` as a browser global for `js/site.js`.

## Existing GitHub implementation reused from bloc-notes-numerique

The browser orchestration pattern and GitHub Actions structure originate from the existing repository `MarcW88/bloc-notes-numerique`, specifically:

- `.agents/skills/site-design-review/scripts/run-visual-review.mjs`
- `.agents/skills/site-design-review/references/playwright-visual-check.md`
- `.github/workflows/visual-design-review.yml`

This repository does not copy the old editorial/design judgments about digital notebooks. Only the technical browser-audit pattern is reused.

## Custom share

There are no locally invented linting, accessibility, Lighthouse or Impeccable rules.

The project-specific layer consists of:

1. parsing `sitemap.xml` to discover the site's own routes;
2. grouping those routes into the existing top-level sections for parallel GitHub Actions jobs;
3. selecting the two viewports already used by the `bloc-notes-numerique` visual-review implementation (1440×1000 and 390×844);
4. knowing that the mobile navigation trigger is `.menu-toggle`;
5. writing upstream outputs and screenshots into `.artifacts/design-audit/`.

That orchestration is deliberately kept below 20% of the audit logic. The analytical rules and scores come from the upstream projects above.

## Local execution

```bash
npm install
npx playwright install chromium

npm run audit:html
npm run audit:css
npm run audit:js
npm run audit:impeccable
npm run audit:visual
npm run audit:lighthouse
```

For a visual subset:

```bash
node .design-audit/run-visual-review.mjs --scope problemen-oplossen
node .design-audit/run-visual-review.mjs --route /verduurzamen/warmtepomp/
```

The visual runner reads `sitemap.xml`; it does not maintain a second custom list of pages.
