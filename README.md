# De Omwenteling

Broncode van de website [omwenteling.com](https://omwenteling.com), een initiatief van
[VBBSKW](https://www.vbbskw.com) rond burgerberaden en democratische vernieuwing in Velsen.

Gebouwd met [Jekyll](https://jekyllrb.com/) en gehost via GitHub Pages.

## Lokaal testen

```
bundle install
bundle exec jekyll serve
```

De site is dan te bekijken op `http://localhost:4000`.

## Nieuwsberichten toevoegen

Zet een bestand in `_posts/`, met bestandsnaam `JJJJ-MM-DD-titel.md` en front matter:

```yaml
---
layout: post
title: "Titel van het bericht"
date: JJJJ-MM-DD
image: /assets/images/jouw-afbeelding.jpg   # optioneel
---
```

Het bericht verschijnt dan automatisch op [`/nieuws.html`](https://omwenteling.com/nieuws.html)
en, als het het nieuwste is, in het "Laatste nieuws"-blok op de homepage.
