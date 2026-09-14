from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'
MANIFEST = ROOT / '.agents' / 'UPSTREAM_SOURCES.json'

if not MANIFEST.exists():
    raise SystemExit('FAIL: .agents/UPSTREAM_SOURCES.json ontbreekt')

manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
verbatim_upstream = {entry['skill'] for entry in manifest.get('skills', [])}

reused_engine = {
    'search-intent',
    'content-refresh',
    'fact-check',
    'affiliate-value',
    'internal-linking-audit',
    'humanizer',
    'general-writing',
    'anti-ai-slop',
    'seo-drift',
    'seo-best-practices',
    'academic-voice',
    'better-usage',
    'brand-analysis-workflow',
    'brand-content-workflow',
    'comparison-analysis-workflow',
    'comparison-content-workflow',
    'content-audit',
    'deal-analysis-workflow',
    'deal-content-workflow',
    'editorial-image-planner',
    'guide-analysis-workflow',
    'guide-content-workflow',
    'jobs-to-be-done',
    'natural-writing',
    'non-autoregressive-writing-pass',
    'site-design-review',
    'trust-content-workflow',
    'usage-analysis-workflow',
    'usage-content-workflow',
    'writing-cadence',
}

custom = {
    'renovation-analysis-workflow',
    'renovation-content-workflow',
    'air-treatment-analysis-workflow',
    'air-treatment-content-workflow',
}

actual = {path.parent.name for path in SKILLS.glob('*/SKILL.md')}
expected = verbatim_upstream | reused_engine | custom

missing = sorted(expected - actual)
unknown = sorted(actual - expected)
if missing:
    raise SystemExit('FAIL: verwachte skills ontbreken: ' + ', '.join(missing))
if unknown:
    raise SystemExit('FAIL: skills zonder policy-classificatie: ' + ', '.join(unknown))

upstream_reused = verbatim_upstream | reused_engine
upstream_count = len(upstream_reused)
custom_count = len(custom)
total = len(actual)
custom_ratio = custom_count / total
upstream_ratio = upstream_count / total

print(
    f'Skills: {total} | upstream/reused={upstream_count} ({upstream_ratio:.1%}) '
    f'| custom={custom_count} ({custom_ratio:.1%})'
)
print(f'- verbatim RampStack: {len(verbatim_upstream)}')
print(f'- reused editorial engine: {len(reused_engine)}')
print(f'- custom orchestration: {len(custom)}')

if custom_ratio > 0.20:
    raise SystemExit(f'FAIL: custom skill ratio {custom_ratio:.1%} is hoger dan 20%')
if upstream_ratio < 0.80:
    raise SystemExit(f'FAIL: upstream/reused ratio {upstream_ratio:.1%} is lager dan 80%')

print('PASS: 80/20 skill policy gerespecteerd')
