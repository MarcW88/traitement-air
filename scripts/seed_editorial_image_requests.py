from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REQUESTS = ROOT / '.content' / 'image-requests'

IMAGES = [
    {
        'id': 'huis-renoveren-startscan',
        'route': 'renovatie-plannen/huis-renoveren',
        'reason': 'Maakt de renovatie-startsituatie en de combinatie van woning, plannen en beslissingen direct concreet.',
        'alt': 'Renovatieplannen op tafel in een gedeeltelijk gerenoveerde woning',
        'prompt': 'A candid editorial photograph inside a believable Dutch family home at the beginning of a renovation. A dining table with architectural sketches, tape measure and material samples, with a partially renovated living space in the background: exposed but tidy wall section, wood, plaster and brick textures, realistic lived-in scale. No readable text, no visible brand, no staged showroom. Warm natural daylight, architectural editorial photography, realistic Dutch residential proportions and materials, subtle imperfections, candid documentary framing, no watermark.'
    },
    {
        'id': 'badkamer-renovatie-context',
        'route': 'renovatieprojecten/badkamer-renovatie',
        'reason': 'Geeft de lezer een realistisch beeld van een badkamer in renovatiefase zonder technische instructie te simuleren.',
        'alt': 'Badkamer tijdens een renovatie met zichtbare afwerking in opbouw',
        'prompt': 'Photorealistic editorial photograph of a small-to-medium Dutch bathroom during renovation, viewed from the doorway. Old finishes partly removed, new neutral wall tiles and sanitary elements waiting to be installed, tidy construction materials, believable plumbing context without close-up technical detail, no people performing risky work. Natural daylight, warm mineral tones, realistic room proportions, candid documentary renovation photography, no visible brand, no readable packaging text, no watermark, not a glossy showroom.'
    },
    {
        'id': 'isolatie-woning-context',
        'route': 'verduurzamen/isolatie',
        'reason': 'Visualiseert isolatie als onderdeel van de gebouwschil zonder één technisch systeem als universele oplossing voor te stellen.',
        'alt': 'Zolder van een woning tijdens isolatiewerken aan het dak',
        'prompt': 'Editorial photograph of a realistic Dutch pitched-roof attic during insulation work. Wide contextual view showing timber rafters, a partly insulated roof plane and a clean work area, with materials shown generically and no branded packaging. Do not depict a detailed technical assembly or step-by-step instruction. Soft natural daylight from a roof window, believable older-home geometry, warm timber and neutral insulation tones, photorealistic documentary style, no readable text, no logo, no watermark.'
    },
    {
        'id': 'warmtepomp-woning-context',
        'route': 'verduurzamen/warmtepomp',
        'reason': 'Laat zien hoe een warmtepomp zich tot een gewone woning en buitenruimte verhoudt zonder een specifiek toestel aan te bevelen.',
        'alt': 'Generieke buitenunit van een warmtepomp naast een Nederlandse woning',
        'prompt': 'Photorealistic editorial exterior of a contemporary but ordinary Dutch terraced or semi-detached home with a generic unbranded air-source heat pump outdoor unit positioned plausibly beside the house. Show the broader garden and facade context rather than installation details. No visible logo, no model markings, no readable labels, no technicians, no unrealistic futuristic architecture. Overcast soft daylight, natural brick and greenery, believable scale, candid architectural photography, no watermark.'
    },
    {
        'id': 'vochtproblemen-signaal',
        'route': 'problemen-oplossen/vochtproblemen',
        'reason': 'Maakt een zichtbaar vochtsignaal herkenbaar terwijl de afbeelding geen oorzaak of diagnose pretendeert te bewijzen.',
        'alt': 'Vochtplek en verkleuring onderaan een binnenmuur',
        'prompt': 'Candid editorial photograph of a realistic interior wall in an older Dutch home showing a modest damp-related visual signal: discoloration and slightly damaged plaster near the lower part of the wall and skirting board. The scene must not imply a diagnosed cause, no dramatic black mold, no fake measurement device reading, no person claiming an inspection result. Natural side light, realistic plaster and flooring textures, documentary home-maintenance photography, no readable text, no branding, no watermark.'
    },
    {
        'id': 'offertes-vergelijken-tafel',
        'route': 'vakman-en-offertes/offertes-vergelijken',
        'reason': 'Ondersteunt de besliscontext van offertes vergelijken met een herkenbaar, niet-commercieel tafelmoment.',
        'alt': 'Huiseigenaren vergelijken renovatieoffertes en plannen aan tafel',
        'prompt': 'Editorial lifestyle photograph of two homeowners at a dining table comparing several renovation quotations, a floor plan and a notebook. Printed pages contain only blurred or non-readable text. The atmosphere is thoughtful and practical, not sales-oriented. Ordinary Dutch home interior, natural daylight, warm neutral materials, candid documentary framing, realistic proportions, no visible company logos, no readable brand names, no watermark, no staged advertising look.'
    },
]


def insert_marker(route: str, marker: str) -> None:
    body_path = ROOT / 'content' / route / 'body.html'
    if not body_path.exists():
        raise SystemExit(f'Missing body: {body_path}')
    text = body_path.read_text(encoding='utf-8')
    if marker in text:
        return
    match = re.search(r'(<p class="content-lead">.*?</p>)', text, flags=re.S)
    if not match:
        raise SystemExit(f'No content-lead found in {body_path}')
    replacement = match.group(1) + '\n\n      ' + marker
    body_path.write_text(text[:match.start()] + replacement + text[match.end():], encoding='utf-8')


def write_request(item: dict) -> None:
    marker = f'<!-- EDITORIAL_IMAGE:{item["id"]} -->'
    route = item['route']
    payload = {
        'id': item['id'],
        'page': f'{route}/index.html',
        'slot': 'editorial',
        'required': True,
        'reason': item['reason'],
        'allow_ai_generation': True,
        'truth_risk': 'LOW',
        'status': 'PENDING',
        'marker': marker,
        'placement': 'replace',
        'output_path': f'assets/generated/{item["id"]}.webp',
        'prompt': item['prompt'],
        'alt': item['alt'],
        'caption': '',
        'width': 1024,
        'height': 672,
        'prompt_upsampling': True,
        'seed': None,
        'generated_at': None,
    }
    REQUESTS.mkdir(parents=True, exist_ok=True)
    target = REQUESTS / f'{item["id"]}.json'
    if target.exists():
        current = json.loads(target.read_text(encoding='utf-8'))
        if current.get('status') == 'GENERATED':
            return
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    insert_marker(route, marker)


for image in IMAGES:
    write_request(image)

print(f'Seeded {len(IMAGES)} editorial image requests.')
