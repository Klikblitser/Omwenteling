#!/usr/bin/env python3
"""Zet de twee variabele bronfonts om naar woff2 die de site zelf serveert.

Aanleiding: assets/css/style.scss haalde Fraunces en Inter bij
fonts.googleapis.com op. Daarmee stuurt de browser van elke bezoeker zijn
IP-adres naar Google voordat er iets te kiezen valt, wat niet strookt met
privacy.md ("verzamelt geen persoonsgegevens van bezoekers"). Beide fonts
staan onder de SIL Open Font License en mogen dus gewoon meeverhuizen.

Draaien:  pip install fonttools brotli && python3 tools/fonts.py

Wat het script doet:
  Fraunces  cursief, wght vastgezet op 600 (de enige snede die de site
            gebruikt, voor de titel). De opsz-as blijft variabel, zodat
            de browser de letter automatisch optisch schaalt.
  Inter     opsz vastgezet op de standaard, wght blijft variabel 400-900.
            Daarmee zijn 700 en 900 uit style.scss echte snedes in plaats
            van door de browser nagebootste vetjes. Onder de 400 gebruikt
            de site niets, dus die kant van de as gaat eruit.
Beide worden gesubset tot latin (U+0000-00FF en wat leestekens). Dat is
genoeg voor Nederlands en voor de Duitse en Franse namen in de teksten.
Latin-ext (Pools, Tsjechisch, Turks) is bewust weggelaten: dat verdubbelt
de bestanden zowat. Zet LATIN_EXT terug in de aanroep als dat ooit nodig
blijkt; een ontbrekend teken valt terug op een systeemletter.
"""
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.environ.get("OMW_ROOT", os.path.dirname(HIER))
BRON = os.path.join(HIER, ".fonts")
DOEL = os.path.join(WORTEL, "assets", "fonts")

# Dezelfde unicode-reeksen die Google Fonts voor latin en latin-ext hanteert.
LATIN = (
    "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
    "U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,"
    "U+2212,U+2215,U+FEFF,U+FFFD"
)
LATIN_EXT = (
    "U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,"
    "U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
)

BRONNEN = {
    "fraunces": "https://github.com/google/fonts/raw/main/ofl/fraunces/"
                "Fraunces-Italic%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf",
    "inter": "https://github.com/google/fonts/raw/main/ofl/inter/"
             "Inter%5Bopsz%2Cwght%5D.ttf",
}

# naam -> (vast te zetten assen, uitvoerbestand)
SNEDES = {
    # De opsz-as van Fraunces blijft staan: de titel schaalt met de
    # vensterbreedte en de browser kiest dan vanzelf de juiste optische
    # snede. Dat kost ongeveer 19 kB en is het waard.
    "fraunces": ({"wght": 600, "SOFT": 0}, "fraunces-italic-600.woff2"),
    "inter": ({"opsz": 14, "wght": (400, 900)}, "inter-variable.woff2"),
}


def haal_bron(naam):
    os.makedirs(BRON, exist_ok=True)
    pad = os.path.join(BRON, naam + ".ttf")
    if not os.path.exists(pad) or os.path.getsize(pad) < 10000:
        subprocess.run(["curl", "-sSL", "-m", "60", "-o", pad, BRONNEN[naam]],
                       check=True)
    return pad


def main():
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer

    os.makedirs(DOEL, exist_ok=True)
    for naam, (assen, bestand) in SNEDES.items():
        bron = haal_bron(naam)
        tussen = os.path.join(BRON, naam + "-instantie.ttf")
        font = TTFont(bron)
        instancer.instantiateVariableFont(font, assen, inplace=True)
        font.save(tussen)

        uit = os.path.join(DOEL, bestand)
        subprocess.run([
            sys.executable, "-m", "fontTools.subset", tussen,
            "--flavor=woff2",
            "--layout-features=*",
            "--unicodes=" + LATIN,
            "--output-file=" + uit,
        ], check=True)
        os.remove(tussen)
        print(f"{bestand}: {os.path.getsize(uit) / 1024:.0f} kB")


if __name__ == "__main__":
    main()
