---
layout: default
---
{% if page.url == '/' %}
  <nav class="paginanav" aria-label="Hoofdnavigatie">
    <a href="{{ '/nieuws.html' | relative_url }}">Nieuws</a>
    <a href="{{ '/handvest.html' | relative_url }}">Handvest</a>
    <a href="{{ '/kleroterion.html' | relative_url }}">Burgerberaden</a>
  </nav>
  {% endif %}

{% if site.posts.size > 0 %}
{% assign laatste = site.posts.first %}
{% assign laatste_afbeelding = laatste.image | default: laatste.thumbnail %}
<div class="laatste-nieuws">
  {% if laatste_afbeelding %}
  <a href="{{ laatste.url | relative_url }}" class="laatste-nieuws-afbeelding">
    <img src="{{ laatste_afbeelding | relative_url }}" alt="{{ laatste.title }}">
  </a>
  {% endif %}
  <div class="laatste-nieuws-tekst">
    <p class="laatste-nieuws-label">Laatste nieuws</p>
    <h3><a href="{{ laatste.url | relative_url }}">{{ laatste.title }}</a></h3>
    <p>{{ laatste.excerpt | strip_html | truncatewords: 30 }}</p>
    <a class="cta-inline" href="{{ laatste.url | relative_url }}">Lees verder</a>
  </div>
</div>
{% endif %}

## Participatieverordening

De gemeente Velsen heeft nog geen participatieverordening vastgesteld. Zij is verplicht om dit te doen voor 1 januari 2027. Eind november komt het voor stemming in de gemeenteraad en is er de mogelijkheid om in te spreken. **Als wij als inwoners zeggenschap willen over hoe deze samenwerking eruit komt te zien, móeten wij van ons laten horen!**

#### Maatschappelijk vastgoed

Om de (culturele) gemeenschap structureel ruimte te bieden, in de breedste zin van het woord, is een opname van een maatschappelijk kader voor vastgoed in de verordening noodzakelijk. Omdat Velsen de verordening van 2022 dus binnen twee maanden moet herzien is dit ons nauwe venster om een recht op maatschappelijk vastgoed te laten opnemen; naar Schots model: een register, een voorkeursperiode die Didam-proof is, en gemeenschapswaarde als gunningscriterium.

#### Burgerberaad als participatiemiddel

De raad kan zijn beslissingsbevoegdheid niet overdragen aan een gelote groep, want een burgerberaad is geen bestuursorgaan. Voor een burgerberaad, met drie kenmerken: gestratificeerde loting, geïnformeerde deliberatie en een schriftelijk advies is (in zelfstandige vorm) beslissingsbevoegheid dus niet haalbaar. Wat wel kan, is zelfbinding van de raad aan procedure en motivering. Daar moet de verordening zich ook op richten.

#### Duurzame participatie

Met een kan-bepaling krijgt de raad de bevoegdheid, maar niet de plicht, om op grond van artikel 84 Gemeentewet een gelote adviescommissie in te stellen. Die commissie bewaakt de kwaliteit, continuïteit en opvolging van burgerberaden en maken we een eerste aanleg naar een geïnstitutionaliseerde, duurzame samenwerking, naar het voorbeeld van de Belgische Duitstalige gemeenschap (Oost-Belgische Model).

### Hoe krijgen inwoners zeggenschap over hun omgeving?

Dat klinkt misschien utopisch maar we geloven dat het mogelijk is door macht te spreiden. Daarvoor moeten we het algemeen handelingsvermogen vergroten en de gemeenschap verheffen. Als de inwoner in het systeem vastloopt kan je nog zoveel workshops, juridische bijstand en cursussen burgerschap bieden; dit repareerd geen kapot systeem. Daarom willen we ook het handelingsperspectief verbeteren door zeggenschap en invloed op een transparante en eerlijke manier te institutionaliseren. Voor dit doel is het burgerberaad als een mes dat aan twee zijden snijd.

## Wat is een burgerberaad?

Een burgerberaad is een groep inwoners, geloot uit de hele gemeente, die zich samen verdiept in een vraagstuk en het lokale bestuur adviseert. Geen verkiezingscampagne, geen partijbelang — een dwarsdoorsnede van de gemeenschap zelf aan tafel.

### Loting naast verkiezingen

Verkiezingen belonen zichtbaarheid; met [loting](https://www.omwenteling.com/kleroterion.html) voegen we daar een tweede vorm van legitimiteit aan toe, gebaseerd op representatie in plaats van populariteit.

### Waarom dit in Velsen gebeurt

Via Stichting De Omwenteling bouwen we in [Velsen](https://omwenteling.com/velsen.html) aan een burgerberaad met een eigen mandaatstructuur en statutair fundament. Het fundament van de organisatie staat met o.a. eisen  en grondslagen beschreven in het [handvest voor de epistemische democratie](https://omwenteling.com/handvest.html) en in het kort nog eens in het [betoog voor de filosofie achter ons initiatief](http://www.omwenteling.com/omwenteling-demo.html).

## Informatiebijeenkomsten & workshops

**Iedereen is welkom** — of je nu alles al weet over deliberatieve democratie of er nog nooit van gehoord hebt. Er is geen voorkennis nodig om aan te sluiten.

### Voor wie

Bewoners van Velsen en omstreken, nieuwsgierigen, twijfelaars, en iedereen die zich weleens heeft afgevraagd of het ook anders kan dan alleen via de stembus.

### Wat je leert

#### Hoe werkt loting?

We laten stap voor stap zien hoe een geloot en representatief samengesteld burgerberaad wordt samengesteld, en waarom dat anders werkt dan een enquête of inspraakavond.

#### Het stratificatie-principe (ook wel gewogen loting genoemd)

Het hoofddoel van dit principe is het creëren van een mini-samenleving of een demografische afspiegeling van de betreffende gemeente, provincie of het land.

#### Deliberatieve democratie in de praktijk

Aan de hand van voorbeelden zoals het burgerberaad in Oost-België (Ostbelgien) en de Connecticut Citizens' Assembly laten we zien hoe beraadslaging in de praktijk tot breed gedragen besluiten leidt.

#### Andere participatiemiddelen

Naast het burgerberaad bespreken we ook het burgerinitiatief en het uitdaagrecht — bestaande instrumenten in de Velsense verordeningen waar je nu al gebruik van kunt maken.

<div class="cta-box" id="aanmelden">
  <h2>Doe mee!</h2>
  <p class="cta-intro">De Omwenteling werkt aan een burgerberaad voor meer zeggenschap van inwoners in Velsen.</p>

  <div class="cta-blok">
    <form action="https://formspree.io/f/xbdlnwpw" method="POST" class="nieuwsbrief-form">
      <label class="nb-label" for="nb-email"><strong>Nieuwsbrief:</strong> blijf op de hoogte van de Omwenteling!</label>
      <div class="nb-rij">
        <input type="email" id="nb-email" name="email" placeholder="uw@email.com" autocomplete="email" required>
        <button type="submit" class="btn">Aanmelden</button>
      </div>
      <label class="nb-toestemming"><input type="checkbox" name="toestemming" value="ja" required> <span>Ik geef toestemming mijn e-mailadres te gebruiken voor de nieuwsbrief van de Omwenteling. Afmelden kan altijd.</span></label>
      <input type="hidden" name="_subject" value="Nieuwe aanmelding nieuwsbrief">
      <input type="hidden" name="_next" value="{{ '/bedankt.html' | absolute_url }}">
      <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
    </form>
  </div>

  <div class="cta-blok">
    <p><strong>Lotingspool:</strong> stel uzelf beschikbaar voor de pool waaruit deelnemers van het burgerberaad worden geloot. Aanmelding verplicht tot niets.</p>
    <a href="{{ '/enquete.html' | relative_url }}" class="btn">Aanmelden (loting of commissie)</a>
  </div>

  <div class="cta-blok">
    <p><strong>Opstartcommissie:</strong> help het proces vormgeven &mdash; communicatie, planning, opdrachtvraag. Via de enqu&ecirc;te: workshop &lsquo;organiseren&rsquo;.</p>
    <a href="{{ '/kleroterion.html' | relative_url }}" class="btn btn-secondary">Meer over loting</a>
  </div>
</div>

## Doe mee

### Meld je aan voor een bijeenkomst

Interesse om aan te sluiten bij een informatiebijeenkomst of workshop? <a class="cta-inline" href="{{ '/contact.html' | relative_url }}">Neem contact op</a>

### Blijf op de hoogte

Lees meer over het [de filosofie achter ons initiatief](http://www.omwenteling.com/omwenteling-demo.html) of over het loting-principe op de [projectpagina voor BURGERBERADEN](https://www.omwenteling.com/kleroterion.html) van Stichtin de Omwenteling.