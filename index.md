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

<div class="cta-box">
  <h2>Doe mee</h2>
  <p>De Omwenteling werkt aan een burgerberaad voor ... in Velsen.
  <form action="https://formspree.io/f/xbdlnwpw" method="POST" class="nieuwsbrief-form">
    <label for="nb-email"><strong>Nieuwsbrief:</strong> blijf op de hoogte van de Omwenteling!</label><br>
    <input type="email" id="nb-email" name="email" placeholder="penningmeester@vbbskw.com" required>
    <button type="submit" class="btn">Aanmelden</button>
    <br>
    <label><input type="checkbox" name="toestemming" value="ja" required> Ik geef toestemming mijn e-mailadres te gebruiken voor de nieuwsbrief van de Omwenteling. Afmelden kan altijd.</label>
    <input type="hidden" name="_subject" value="Nieuwe aanmelding nieuwsbrief">
    <input type="hidden" name="_next" value="{{ '/bedankt.html' | absolute_url }}">
    <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
  </form>
  <p><strong>Lotingspool:</strong> stel uzelf beschikbaar voor de pool waaruit deelnemers van het burgerberaad worden geloot. Aanmelding verplicht tot niets.<br>
  <a href="{{ '/enquete.html' | relative_url }}" class="btn">Aanmelden (loting of commissie)</a>
  <strong>Opstartcommissie:</strong> help het proces vormgeven &mdash; communicatie, planning, opdrachtvraag. Via de enquête: workshop &lsquo;organiseren&rsquo;.</p>
  <a href="{{ '/kleroterion.html' | relative_url }}" class="btn btn-secondary">Meer over loting</a>
</div>

## Doe mee

### Meld je aan voor een bijeenkomst

Interesse om aan te sluiten bij een informatiebijeenkomst of workshop? <a class="cta-inline" href="{{ '/contact.html' | relative_url }}">Neem contact op</a>

### Blijf op de hoogte

Lees meer over het [de filosofie achter ons initiatief](http://www.omwenteling.com/omwenteling-demo.html) of over het loting-principe op de [projectpagina voor BURGERBERADEN](https://www.omwenteling.com/kleroterion.html) van Stichtin de Omwenteling.