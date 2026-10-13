# Skizzen für Postings

`skizzen_bauen.cjs` erzeugt `../skizzen-sektionen.html` (sechs Skizzen-Postings), die `postings_vorlage_bauen.py` einbindet.

Benötigt ein Node-Projekt mit: `@opeepsfun/open-peeps@1.0.6`, `react@18`, `react-dom@18`, `roughjs@4.6.6`, `esbuild`.
`composer.mjs` wird mit `npx esbuild composer.mjs --bundle --platform=node --outfile=composer.cjs` gebündelt (setzt Open-Peeps-Figuren statisch zusammen).

Lizenzen: Open Peeps (Pablo Stanley) CC0 · rough.js MIT · Caveat (Google Fonts) SIL Open Font License.
Farben: Hauttöne und Fremdfarben werden auf Weiß/Gelb umgefärbt; keine KI-Bilder.
