#!/usr/bin/env python3
"""Genereert de deelafbeelding (og:image) voor WhatsApp, Signal en andere
link-previews: assets/images/og-omwenteling.png, 1200x630.

De afbeelding herhaalt bewust de koptekst van de site: Fraunces cursief,
de logo-O als letter, de kleuren uit assets/css/style.scss. Alles staat
binnen de middelste 80% van het doek, omdat WhatsApp alles wat niet
1.91:1 is vanuit het midden bijsnijdt.

Draaien:  python3 tools/og-image.py
De twee variabele fonts worden eenmalig opgehaald naar tools/.fonts/ en
staan in .gitignore; ze horen niet in de repo thuis.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTMAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".fonts")
UIT = os.path.join(WORTEL, "assets", "images", "og-omwenteling.png")
LOGO = os.path.join(WORTEL, "assets", "images", "logo-o.png")

FONTS = {
    "fraunces": "https://github.com/google/fonts/raw/main/ofl/fraunces/"
                "Fraunces-Italic%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf",
    "inter": "https://github.com/google/fonts/raw/main/ofl/inter/"
             "Inter%5Bopsz%2Cwght%5D.ttf",
}

BREEDTE, HOOGTE = 1200, 630
PAPIER = "#faf9f6"      # body-achtergrond
INKT = "#000000"        # kleur van de titel
DIEPROOD = "#6f1f1f"    # linkkleur, gebruikt voor de onderregel
SIGNAALROOD = "#e83d3d" # accent uit de ribbon
DONKER = "#211616"      # ribbon- en footerkleur
BAND_H = 92

TITEL_PT = 118
ONDERREGEL = "Informatiebijeenkomsten en workshops over burgerberaden"
DOMEIN = "omwenteling.com"


def haal_fonts():
    os.makedirs(FONTMAP, exist_ok=True)
    paden = {}
    for naam, url in FONTS.items():
        pad = os.path.join(FONTMAP, naam + ".ttf")
        if not os.path.exists(pad) or os.path.getsize(pad) < 10000:
            subprocess.run(["curl", "-sSL", "-m", "60", "-o", pad, url], check=True)
        paden[naam] = pad
    return paden


def stel_gewicht_in(font, **assen):
    """Zet de assen van een variabel font op de gevraagde waarden."""
    namen = [as_["name"].decode() if isinstance(as_["name"], bytes) else as_["name"]
             for as_ in font.get_variation_axes()]
    waarden = [as_["default"] for as_ in font.get_variation_axes()]
    for i, naam in enumerate(namen):
        sleutel = naam.strip().lower().replace(" ", "")
        if sleutel in assen:
            waarden[i] = assen[sleutel]
    font.set_variation_by_axes(waarden)
    return font


def main():
    paden = haal_fonts()

    titel = ImageFont.truetype(paden["fraunces"], TITEL_PT)
    stel_gewicht_in(titel, weight=600, opticalsize=144, softness=0, wonky=0)

    sub = ImageFont.truetype(paden["inter"], 30)
    stel_gewicht_in(sub, weight=600, opticalsize=32)

    klein = ImageFont.truetype(paden["inter"], 27)
    stel_gewicht_in(klein, weight=600, opticalsize=28)

    doek = Image.new("RGB", (BREEDTE, HOOGTE), PAPIER)
    tek = ImageDraw.Draw(doek)

    # --- titelregel: "De" + logo-O + "mwenteling" ---------------------------
    links, rechts = "De ", "mwenteling"
    b_links = tek.textlength(links, font=titel)
    b_rechts = tek.textlength(rechts, font=titel)
    logo_h = int(TITEL_PT * 1.8)
    logo = Image.open(LOGO).convert("RGBA")
    logo_b = int(logo.width * logo_h / logo.height)
    logo = logo.resize((logo_b, logo_h), Image.LANCZOS)

    totaal = b_links + logo_b + b_rechts
    x = (BREEDTE - totaal) / 2
    basislijn = 330

    tek.text((x, basislijn), links, font=titel, fill=INKT, anchor="ls")
    # vertical-align: -0.35em, net als in style.scss
    doek.paste(logo, (int(x + b_links), int(basislijn + 0.35 * TITEL_PT - logo_h)), logo)
    tek.text((x + b_links + logo_b, basislijn), rechts, font=titel, fill=INKT, anchor="ls")

    # --- rode streep --------------------------------------------------------
    streep_b = 150
    tek.rectangle(
        [(BREEDTE - streep_b) / 2, 396, (BREEDTE + streep_b) / 2, 399],
        fill=SIGNAALROOD,
    )

    # --- onderregel ---------------------------------------------------------
    tek.text((BREEDTE / 2, 452), ONDERREGEL, font=sub, fill=DIEPROOD, anchor="ms")

    # --- donkere band met het domein ---------------------------------------
    tek.rectangle([0, HOOGTE - BAND_H, BREEDTE, HOOGTE], fill=DONKER)
    tek.text((BREEDTE / 2, HOOGTE - BAND_H / 2), DOMEIN, font=klein,
             fill=PAPIER, anchor="mm")

    doek.save(UIT, "PNG", optimize=True)
    kb = os.path.getsize(UIT) / 1024
    print(f"{UIT} -> {BREEDTE}x{HOOGTE}, {kb:.0f} kB")
    if kb > 300:
        print("LET OP: groter dan 300 kB", file=sys.stderr)


if __name__ == "__main__":
    main()
