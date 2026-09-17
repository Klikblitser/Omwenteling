---
layout: default
title: Contact
permalink: /contact.html
leaflet: true
---

## Contact

Heeft u vragen over de Stichting De Omwenteling of wilt jij je aansluiten? Neem gerust contact met ons op.

<div class="contact-grid" markdown="1">
  <div class="contact-info" markdown="1">

### Contactgegevens

<div class="contact-item">
  <span>✉️</span>
  <div>
    <strong>E-mail</strong><br>
    <a href="mailto:voorzitter@vbbskw.com">voorzitter@vbbskw.com</a>
  </div>
</div>

<div class="contact-item">
  <span>🏠</span>
  <div>
    <strong>Locatie</strong><br>
    Noordersluisweg 16A<br>
    1975AM<br>
    IJmuiden
  </div>
</div>

### Lid worden?

Stuur een e-mail naar <a href="mailto:voorzitter@vbbskw.com">voorzitter@vbbskw.com</a>, dan ontvang je de statuten en het inschrijfformulier.

  </div>

  <div class="map-container" markdown="1">

### Locatie

<div id="map"></div>

<p class="privacy-note">De kaart komt van OpenStreetMap. Uw browser maakt daarvoor rechtstreeks verbinding met servers van de OpenStreetMap Foundation, waarbij uw IP-adres bij die stichting terechtkomt. <a href="/privacy.html#kaart">Meer info</a></p>

  </div>
</div>

[⬅️ Terug naar de hoofdpagina](./)

<script src="{{ '/assets/vendor/leaflet/1.9.4/leaflet.js' | relative_url }}"></script>
<script>
  // Coördinaten voor Binnenspuikanaal, IJmuiden
  var lat = 52.469634;
  var lon = 4.604854;

  var map = L.map('map').setView([lat, lon], 15);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);

  L.marker([lat, lon]).addTo(map)
    .bindPopup('<strong>VBBSKW</strong><br>Binnenspuikanaal West')
    .openPopup();
</script>
