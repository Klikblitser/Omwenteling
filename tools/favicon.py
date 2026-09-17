#!/usr/bin/env python3
"""Maakt het tabbladpictogram uit assets/images/logo-o.png.

Uitvoer in de wortel van de site, want daar zoeken browsers en iOS ze uit
zichzelf, ook zonder link-tag:

  favicon.ico          16, 32 en 48 pixels in een bestand, met doorzichtige
                       achtergrond, zodat het logo op een licht en een donker
                       tabblad allebei werkt
  apple-touch-icon.png 180 pixels, dichte achtergrond in de papierkleur van
                       de site; iOS kan niet met doorzichtigheid overweg en
                       zet er anders zwart achter

Draaien:  python3 tools/favicon.py
"""
import os

from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.environ.get("OMW_ROOT", os.path.dirname(HIER))
LOGO = os.path.join(WORTEL, "assets", "images", "logo-o.png")
PAPIER = (250, 249, 246, 255)   # #faf9f6, gelijk aan de body-achtergrond

ICO_MATEN = [16, 32, 48]
LUCHT_TAB = 0.02      # marge rondom in het tabblad
LUCHT_IOS = 0.14      # iOS snijdt de hoeken af, dus daar wat meer


def vierkant(bron, lucht, achtergrond=None):
    """Snijdt het logo bij tot zijn eigen randen en zet het gecentreerd op
    een vierkant doek met de opgegeven marge."""
    logo = Image.open(bron).convert("RGBA")
    logo = logo.crop(logo.getchannel("A").getbbox())

    zijde = max(logo.size)
    doek_zijde = int(round(zijde / (1 - 2 * lucht)))
    doek = Image.new("RGBA", (doek_zijde, doek_zijde),
                     achtergrond or (0, 0, 0, 0))
    doek.paste(logo, ((doek_zijde - logo.width) // 2,
                      (doek_zijde - logo.height) // 2), logo)
    return doek


def main():
    tab = vierkant(LOGO, LUCHT_TAB)
    ico = os.path.join(WORTEL, "favicon.ico")
    # Pillow schaalt zelf naar elk formaat in de lijst; LANCZOS houdt de
    # dunne zwarte omlijning van de pijlen op 16 pixels nog net heel.
    tab.resize((256, 256), Image.LANCZOS).save(
        ico, sizes=[(m, m) for m in ICO_MATEN])

    ios = vierkant(LOGO, LUCHT_IOS, PAPIER).resize((180, 180), Image.LANCZOS)
    ios_pad = os.path.join(WORTEL, "apple-touch-icon.png")
    ios.convert("RGB").save(ios_pad, "PNG", optimize=True)

    for pad in (ico, ios_pad):
        print(f"{os.path.basename(pad)}: {os.path.getsize(pad) / 1024:.1f} kB")


if __name__ == "__main__":
    main()
