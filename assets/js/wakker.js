/* Typmachine-effect voor elementen met data-typen.
   De tekst staat gewoon in de HTML; zonder JavaScript of met "minder
   beweging" aan blijft hij in een keer zichtbaar. Het script verpakt elke
   letter in een span die al ruimte inneemt, zodat de regel niet verspringt
   terwijl hij "getypt" wordt. */
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  document.querySelectorAll('[data-typen]').forEach(function (el) {
    var tekst = el.textContent.replace(/\s+/g, ' ').trim();
    el.setAttribute('aria-label', tekst);
    el.textContent = '';

    var letters = [];
    tekst.split(' ').forEach(function (woord, i, woorden) {
      // Woorden blijven heel, zodat de regel alleen tussen woorden breekt.
      var w = document.createElement('span');
      w.style.whiteSpace = 'nowrap';
      w.setAttribute('aria-hidden', 'true');
      Array.from(woord).forEach(function (teken) {
        var s = document.createElement('span');
        s.className = 'letter';
        s.textContent = teken;
        w.appendChild(s);
        letters.push(s);
      });
      el.appendChild(w);
      if (i < woorden.length - 1) el.appendChild(document.createTextNode(' '));
    });

    var i = 0;
    function volgende() {
      if (i > 0) letters[i - 1].classList.remove('cursor');
      if (i >= letters.length) {
        var laatste = letters[letters.length - 1];
        laatste.classList.add('cursor');
        setTimeout(function () { laatste.classList.remove('cursor'); }, 2600);
        return;
      }
      letters[i].classList.add('getypt', 'cursor');
      i++;
      // Een typmachine heeft geen gelijkmatig ritme.
      setTimeout(volgende, 45 + Math.random() * 70);
    }
    setTimeout(volgende, 350);
  });
})();
