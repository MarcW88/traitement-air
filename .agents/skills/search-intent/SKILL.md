---
name: search-intent
description: Bewaak zoekintentie, paginafunctie en cannibalisatie voor renovatiecontent op thuisrenovatie-gids.nl.
license: MIT
provenance: upstream
upstream: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/search-intent
---

# Search intent — thuisrenovatie-gids.nl

## Doel

Een inhoudelijk correcte renovatiepagina is niet goed genoeg wanneer ze de verkeerde taak of beslissing bedient. Gebruik deze skill om vóór briefing of rewrite vast te leggen wat de gebruiker werkelijk probeert te begrijpen, beslissen, controleren of uitvoeren.

## Bepaal eerst

Voor elke URL:

- primaire query of querygroep;
- dominante intentie: informationeel, commercieel onderzoek, transactioneel of navigerend;
- concrete gebruikersbeslissing of taak;
- correcte paginafunctie binnen de site;
- belangrijkste vervolgvraag;
- maturiteitsniveau: oriënteren, plannen, vergelijken, uitvoeren of probleem oplossen.

Gebruik semantische analyse, GSC, SERP-data en bestaande briefs wanneer beschikbaar. Raad de targetquery niet wanneer betere data beschikbaar is.

## Sitefuncties

De routefamilie bepaalt de redactionele grens, niet de artikelstructuur:

- `renovatie-plannen/`: scope, prioriteiten, volgorde, budget, fasering, regels en rendement;
- `renovatieprojecten/`: beslissingen rond een concreet renovatieproject;
- `verduurzamen/`: energie-, comfort- en installatiekeuzes;
- `problemen-oplossen/`: symptoom, oorzaak, veilige diagnose en oplossing;
- `doe-het-zelf/`: uitvoerbare taak met duidelijke veiligheidsgrens;
- `vakman-en-offertes/`: vakmanselectie, offertekwaliteit, vergelijking en leadbeslissing.

Wanneer de echte intentie beter in een andere routefamilie past, forceer de tekst niet in de bestaande slug. Flag de grens voor `renovation-analysis-workflow`.

## On-page regels

- Titel en H1 ondersteunen dezelfde hoofdintentie zonder mechanische exact-match-eis.
- De kernvraag wordt vroeg beantwoord wanneer de intentie dat vereist.
- H2's bestaan omdat ze een echte deelvraag, beslissing, afhankelijkheid, uitzondering of noodzakelijke stap behandelen.
- Voeg geen headings toe enkel voor keywordvarianten.
- Een prijs-, subsidie-, vergunnings- of rendementsterm maakt een pagina niet automatisch transactioneel.
- Interne links ondersteunen de volgende logische beslissing, niet een quota.
- Meta descriptions zijn voor duidelijkheid en CTR, niet voor keyword stuffing.
- Geen verplichte woordenaantallen.

## Cannibalisatiecheck

Flag wanneer meerdere URL's dezelfde primaire taak of beslissing lijken te bedienen. Geef aan:

- welke URL waarschijnlijk eigenaar van de intentie moet zijn;
- welke unieke taak of grens de andere URL nodig heeft;
- of `MERGE` waarschijnlijk beter is;
- of het probleem alleen in title/H1/positionering zit of structureel is.

Een praktische test: wanneer twee pagina's dezelfde centrale conclusie, dezelfde besliscriteria en grotendeels dezelfde secties kunnen behouden door alleen het onderwerp te vervangen, is de scheiding waarschijnlijk onvoldoende.

## Output

1. **Primary intent**
2. **Primary query/topic**
3. **User decision/problem**
4. **Correct route family / page role**
5. **Intent gaps**
6. **Sections that do not serve intent**
7. **Next-question / internal-link opportunities**
8. **Cannibalization risk**
9. **Unknowns that can change the decision**
