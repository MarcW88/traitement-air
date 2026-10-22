---
name: content-refresh
description: Bepaal hoe bestaande renovatiecontent gericht moet worden hersteld zonder automatisch alles te herschrijven.
license: MIT
provenance: upstream
upstream: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/content-refresh
---

# Content refresh — thuisrenovatie-gids.nl

Gebruik alleen nadat `renovation-analysis-workflow / AUDIT` heeft vastgesteld dat een pagina een update nodig heeft.

## Principe

Behoud wat goed is. Herstel het probleem, niet automatisch de hele tekst.

## Diagnose

Classificeer de belangrijkste oorzaak:

- **Intent drift:** de pagina beantwoordt niet meer de dominante zoek- of gebruikstaak.
- **Thin value:** correcte maar oppervlakkige informatie zonder echte beslissingswaarde.
- **Outdated:** prijzen, subsidies, vergunningen, regelgeving, technische prestaties, product-/installatiegegevens of procedures zijn verouderd.
- **Weak structure:** cruciale informatie staat te laat, is versnipperd of maakt de beslissing moeilijker.
- **Cannibalization:** overlap met een andere URL of een fout afgebakende clusterrol.
- **Generic prose:** veel tekst maar weinig concrete informatie, afhankelijkheden, uitzonderingen of beslisregels.
- **Trust gap:** centrale claims zijn onvoldoende onderbouwd of te stellig geformuleerd.
- **Safety gap:** risicovolle werkzaamheden worden te eenvoudig voorgesteld of missen stopcondities.
- **Conversion distortion:** de CTA stuurt te vroeg naar een offerte of vakman en vervangt inhoudelijke hulp.
- **Structural cloning:** de pagina herhaalt het format, de H2-functies, tabellen of conclusies van andere pagina's zonder inhoudelijke noodzaak.

## Refreshniveau

### Light edit

Voor kleine actualisaties, ontbrekende bronverwijzingen, slechte passages, metadata, een lokale grens of enkele ontbrekende antwoorden. Behoud zoveel mogelijk valide inhoud en structuur.

### Major revision

Voor een goede URL met structurele inhoudsgaten. Herbouw alleen de delen die nodig zijn en behoud sterke passages, bewezen voorbeelden, nuttige links en correcte feiten.

### Full rewrite

Alleen wanneer de huidige tekst grotendeels generiek, verkeerd gericht, sterk gekloond, feitelijk onbetrouwbaar of onveilig is. De URL en intentie blijven behouden tenzij `renovation-analysis-workflow` anders beslist.

## Renovatiespecifieke controle

Controleer waar relevant of de pagina duidelijk maakt:

- welke beslissing of taak centraal staat;
- welke woningcontext of aannames de uitkomst veranderen;
- welke afhankelijkheden eerst moeten worden opgelost;
- wat stabiele kennis is en wat tijd-/regiogebonden is;
- wanneer een vakman of specialist nodig is;
- wat de gebruiker beter niet zelf doet;
- welke prijs- of rendementclaims alleen indicatief kunnen zijn;
- welke informatie opnieuw gecontroleerd moet worden vóór publicatie.

## Niet doen

- extra FAQ's toevoegen puur voor SEO;
- alle headings vervangen omdat een model een gelijkmatiger structuur wil;
- elke keywordvariant forceren;
- concrete informatie vervangen door vage, vloeiende tekst;
- een bestaande pagina volledig herschrijven wanneer een gerichte correctie volstaat;
- een standaard PLAN/PROJECT/DIY-template opleggen.

## Output

Lever eerst een refresh plan met:

1. wat blijft;
2. wat wordt verwijderd;
3. wat wordt herschreven;
4. welke nieuwe informatie nodig is;
5. welke claims eerst onderzocht moeten worden;
6. veiligheids- of trustrisico's;
7. aanbevolen refreshniveau.
