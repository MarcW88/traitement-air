---
name: fact-check
description: Verifieer claims in renovatiecontent in een aparte pass vóór publicatie.
license: MIT
provenance: upstream
upstream: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/fact-check
---

# Fact check — thuisrenovatie-gids.nl

Deze pass staat los van schrijven. Een renovatieclaim is niet betrouwbaar omdat hij plausibel klinkt.

## Claims die altijd gecontroleerd moeten worden wanneer ze voorkomen

- prijzen, kostenbandbreedtes en prijs per m²;
- subsidies, premies, fiscale voordelen en voorwaarden;
- vergunningen, meldingsplichten en lokale regels;
- technische normen, certificaten en wettelijke eisen;
- isolatiewaarden, energieprestaties, rendementen en terugverdientijden;
- product- en installatiespecificaties;
- veiligheidsclaims;
- levensduur, onderhoudsintervallen en garantie;
- vergelijkende claims zoals goedkoper, duurzamer, sneller, efficiënter of waardeverhogend;
- beschikbaarheid of voorwaarden van diensten en offertes;
- markt- of regiogebonden uitspraken.

## Bronnenhiërarchie

1. overheid, wetgeving, officiële loketten en bevoegde instanties;
2. officiële technische documentatie, normenorganisaties of fabrikantdocumentatie voor productspecifieke feiten;
3. onafhankelijke vakorganisaties, kenniscentra en betrouwbare onderzoeksbronnen;
4. marktdata of meerdere betrouwbare commerciële bronnen voor actuele prijsindicaties;
5. gebruikerservaring alleen voor ervaringspatronen, nooit als vervanging van regels of technische feiten.

Gebruik geen andere affiliate- of leadsite als primaire bron wanneer een sterkere bron beschikbaar is.

## Proces

1. Extraheer alle verifieerbare claims.
2. Label elke claim als hard fact, soft fact, vergelijking, ervaring, inschatting of advies.
3. Noteer voor tijd- of regiogebonden claims markt/regio en controledatum.
4. Zoek een passende bron voor elke belangrijke claim.
5. Geef status:
   - `CONFIRMED`
   - `PARTIAL`
   - `UNVERIFIED`
   - `CONTRADICTED`
   - `OUTDATED`
6. Corrigeer alleen op basis van bewijs.
7. Laat onzekerheid zichtbaar; vul gaten niet op met modelkennis.
8. Controleer na latere tekstwijzigingen opnieuw alle nieuw geïntroduceerde claims.

## Renovatiespecifieke grens

- Een landelijke regel mag niet worden voorgesteld als lokale regel zonder controle.
- Een subsidiebedrag of voorwaarde krijgt altijd een actuele bron en datum.
- Een prijsrange moet duidelijk maken waarop hij betrekking heeft en welke factoren de range kunnen veranderen.
- Een technisch rendement zonder context, aannames of meetcondities is geen betrouwbare claim.
- Een veiligheidswaarschuwing mag niet worden afgezwakt om de tekst vloeiender of commerciëler te maken.
- Schrijf nooit alsof de site een woning, installatie of schade ter plaatse heeft geïnspecteerd wanneer dat niet zo is.

## Output

Maak een compact verificatielog:

| Claim | Status | Source | Checked | Scope/conditions | Action |
|---|---|---|---|---|---|

Eindig met:

- **Overall confidence**
- **Corrections required**
- **Claims to remove or qualify if unverifiable**
- **Time-sensitive claims that need a future refresh**
