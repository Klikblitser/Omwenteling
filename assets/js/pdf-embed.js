/*
 * pdf-embed.js — rendert PDF's rechtstreeks in de paginaflow met pdf.js.
 *
 * Waarom niet <object>/<iframe>: mobiele browsers (Chrome en Firefox op
 * Android, alle browsers op iOS) weigeren een PDF inline te tonen en bieden
 * in plaats daarvan een download aan. pdf.js tekent de pagina's zelf op een
 * canvas, dus de weergave is op elk apparaat identiek.
 *
 * Gebruik:  <div class="pdf-embed" data-pdf="/assets/documenten/x.pdf"></div>
 * Zie _includes/pdf-viewer.html.
 */

import * as pdfjsLib from './pdfjs/pdf.min.js';

const HERE = new URL('.', import.meta.url);

pdfjsLib.GlobalWorkerOptions.workerSrc =
  new URL('pdfjs/pdf.worker.min.js', HERE).href;

const STANDARD_FONT_DATA_URL = new URL('pdfjs/standard_fonts/', HERE).href;

/* Hoeveel scherm-pixels per CSS-pixel we tekenen. Op telefoons is de
   device pixel ratio vaak 3 of 4; dat afkappen op 2 scheelt aanzienlijk
   geheugen zonder zichtbaar kwaliteitsverlies. */
const MAX_PIXEL_RATIO = 2;

/* Marge rond de viewport waarbinnen pagina's alvast gerenderd worden. */
const PRERENDER_MARGIN = '150% 0px';

const supportsIO = 'IntersectionObserver' in window;

function el(tag, className, parent) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (parent) parent.appendChild(node);
  return node;
}

class PdfPage {
  constructor(doc, pageNumber, container) {
    this.doc = doc;
    this.pageNumber = pageNumber;
    this.page = null;
    this.rendered = false;
    this.renderTask = null;
    this.textLayer = null;
    this.width = 0;

    this.root = el('div', 'pdf-embed__page', container);
    this.root.setAttribute('role', 'img');
    this.root.setAttribute('aria-label', `Pagina ${pageNumber}`);
  }

  /* Reserveert de juiste hoogte zodat de pagina niet verspringt zodra
     hij daadwerkelijk gerenderd wordt. */
  async prepare() {
    this.page = await this.doc.getPage(this.pageNumber);
    const vp = this.page.getViewport({ scale: 1 });
    this.root.style.aspectRatio = `${vp.width} / ${vp.height}`;
    this.ratio = vp.width / vp.height;
  }

  cancel() {
    if (this.renderTask) {
      try { this.renderTask.cancel(); } catch (_) { /* al klaar */ }
      this.renderTask = null;
    }
  }

  /* Geeft canvasgeheugen terug wanneer de pagina ver buiten beeld is.
     Zonder dit loopt een document van tientallen pagina's op een telefoon
     vast op geheugengebrek. */
  unrender() {
    this.cancel();
    if (!this.rendered) return;
    this.rendered = false;
    if (this.canvas) {
      this.canvas.width = 0;
      this.canvas.height = 0;
      this.canvas.remove();
      this.canvas = null;
    }
    if (this.textDiv) {
      this.textLayer = null;
      this.textDiv.remove();
      this.textDiv = null;
    }
  }

  async render() {
    const cssWidth = this.root.clientWidth;
    if (!cssWidth) return;
    if (this.rendered && this.width === cssWidth) return;

    this.cancel();
    this.width = cssWidth;

    const dpr = Math.min(window.devicePixelRatio || 1, MAX_PIXEL_RATIO);
    const base = this.page.getViewport({ scale: 1 });
    const cssScale = cssWidth / base.width;

    const viewportCss = this.page.getViewport({ scale: cssScale });
    const viewportDev = this.page.getViewport({ scale: cssScale * dpr });

    if (!this.canvas) this.canvas = el('canvas', 'pdf-embed__canvas', this.root);
    this.canvas.width = Math.floor(viewportDev.width);
    this.canvas.height = Math.floor(viewportDev.height);
    this.canvas.style.width = '100%';
    this.canvas.style.height = 'auto';

    const ctx = this.canvas.getContext('2d', { alpha: false });

    this.renderTask = this.page.render({
      canvas: this.canvas,
      canvasContext: ctx,
      viewport: viewportDev,
    });

    try {
      await this.renderTask.promise;
    } catch (err) {
      if (err && err.name === 'RenderingCancelledException') return;
      throw err;
    }
    this.renderTask = null;
    this.rendered = true;

    /* Tekstlaag: onzichtbare, exact gepositioneerde spans boven het canvas.
       Daardoor blijft de tekst selecteerbaar, doorzoekbaar met Ctrl+F en
       leesbaar voor schermlezers. */
    try {
      if (this.textDiv) this.textDiv.remove();
      this.textDiv = el('div', 'pdf-embed__text textLayer', this.root);
      /* pdf.js positioneert de spans in procenten van de laag; de laag zelf
         krijgt zijn afmetingen via deze schaalfactor (zie pdf-embed.css). */
      this.textDiv.style.setProperty('--scale-factor', cssScale);

      this.textLayer = new pdfjsLib.TextLayer({
        textContentSource: this.page.streamTextContent(),
        container: this.textDiv,
        viewport: viewportCss,
      });
      await this.textLayer.render();
      this.root.removeAttribute('role');
      this.root.removeAttribute('aria-label');
    } catch (_) {
      /* Zonder tekstlaag blijft het canvas gewoon zichtbaar. */
    }
  }
}

class PdfEmbed {
  constructor(container) {
    this.container = container;
    this.url = container.dataset.pdf;
    this.pages = [];
    this.started = false;
    this.status = container.querySelector('.pdf-embed__status');
    this.pagesEl = el('div', 'pdf-embed__pages', container);
    container.insertBefore(this.pagesEl, container.querySelector('.pdf-embed__foot'));
  }

  setStatus(text, isError) {
    if (!this.status) return;
    this.status.textContent = text || '';
    this.status.hidden = !text;
    this.status.classList.toggle('pdf-embed__status--error', !!isError);
  }

  async start() {
    if (this.started) return;
    this.started = true;
    this.setStatus('Document wordt geladen…');

    try {
      const doc = await pdfjsLib.getDocument({
        url: this.url,
        standardFontDataUrl: STANDARD_FONT_DATA_URL,
      }).promise;

      this.doc = doc;
      this.container.dataset.pages = doc.numPages;

      for (let i = 1; i <= doc.numPages; i++) {
        const page = new PdfPage(doc, i, this.pagesEl);
        this.pages.push(page);
      }
      await Promise.all(this.pages.map((p) => p.prepare()));
      this.setStatus('');

      this.observePages();
      this.observeResize();
    } catch (err) {
      console.error('[pdf-embed]', err);
      this.setStatus(
        'Dit document kon niet in de pagina worden weergegeven. Gebruik de downloadlink hieronder.',
        true
      );
      this.container.classList.add('pdf-embed--failed');
    }
  }

  observePages() {
    if (!supportsIO) {
      this.pages.forEach((p) => p.render());
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          const page = entry.target.__pdfPage;
          if (!page) continue;
          if (entry.isIntersecting) page.render().catch(() => {});
          else page.unrender();
        }
      },
      { rootMargin: PRERENDER_MARGIN }
    );
    for (const page of this.pages) {
      page.root.__pdfPage = page;
      io.observe(page.root);
    }
    this.io = io;
  }

  /* Bij het draaien van een telefoon of het verslepen van een vensterrand
     verandert de breedte; het canvas moet dan opnieuw scherp getekend worden. */
  observeResize() {
    let timer = null;
    let lastWidth = this.pagesEl.clientWidth;

    const redraw = () => {
      const width = this.pagesEl.clientWidth;
      if (width === lastWidth) return;
      lastWidth = width;
      for (const page of this.pages) {
        if (page.rendered) {
          page.rendered = false;
          page.render().catch(() => {});
        }
      }
    };

    const schedule = () => {
      clearTimeout(timer);
      timer = setTimeout(redraw, 200);
    };

    if ('ResizeObserver' in window) {
      new ResizeObserver(schedule).observe(this.pagesEl);
    } else {
      window.addEventListener('resize', schedule);
      window.addEventListener('orientationchange', schedule);
    }
  }
}

function init() {
  const containers = document.querySelectorAll('.pdf-embed[data-pdf]');
  if (!containers.length) return;

  for (const container of containers) {
    const embed = new PdfEmbed(container);

    /* Pas laden zodra het document in de buurt van het scherm komt: op een
       pagina met meerdere documenten scheelt dat onnodig dataverkeer. */
    if (supportsIO) {
      const io = new IntersectionObserver(
        (entries) => {
          if (entries.some((e) => e.isIntersecting)) {
            io.disconnect();
            embed.start();
          }
        },
        { rootMargin: '300px 0px' }
      );
      io.observe(container);
    } else {
      embed.start();
    }
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
