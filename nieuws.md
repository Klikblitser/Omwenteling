---
layout: default
title: Nieuws
---

## Nieuws

{% if site.posts.size == 0 %}
<p>Er zijn nog geen nieuwsberichten geplaatst.</p>
{% endif %}

{% for post in site.posts %}
<div class="nieuws-item">
  <p class="nieuws-datum">{{ post.date | date: "%d-%m-%Y" }}</p>
  <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  <p>{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
  <a class="nieuws-lees-meer" href="{{ post.url | relative_url }}">Lees verder →</a>
</div>
{% endfor %}

[⬅️ Terug naar de hoofdpagina](./)
