(() => {
  const LOGO_PATHS = `
    <path fill="#F25022" d="M532 131 L36 462 L13 497 L13 560 L23 582 L48 604 L521 923 L539 926 L539 699 L547 680 L314 530 L527 395 L551 371 L558 347 L558 155 L547 135 Z"/>
    <path fill="#7FBA00" d="M551 681 L542 693 L540 700 L540 917 L546 930 L558 940 L571 943 L778 943 L788 941 L798 935 L809 910 L809 702 L807 694 L799 682 L784 674 L566 674 Z"/>
    <path fill="#FFB900" d="M1390 16 L1208 13 L1184 23 L1171 38 L768 1009 L768 1026 L778 1038 L957 1042 L975 1037 L995 1017 L1346 179 L1349 145 L1367 129 L1401 47 L1402 31 Z"/>
    <path fill="#00A4EF" d="M1369 131 L1350 149 L1349 355 L1354 369 L1385 399 L1592 528 L1373 667 L1354 688 L1349 703 L1349 907 L1361 924 L1377 926 L1871 595 L1893 563 L1894 501 L1885 477 L1863 456 L1398 142 Z"/>`;

  const CONFIG = {
    pt: { path: '', label: 'PT', code: 'pt-BR' },
    en: { path: 'en/', label: 'EN', code: 'en' },
    es: { path: 'es/', label: 'ES', code: 'es' }
  };

  const body = document.body;
  const app = document.getElementById('app');
  const pageLang = body.dataset.lang || 'pt-BR';
  const basePath = body.dataset.base || '';
  const contentPath = body.dataset.content || `${basePath}content.json`;
  const shouldAutodetect = body.dataset.autodetect === 'true';

  function detectBrowserLanguage() {
    const raw = (navigator.languages && navigator.languages[0]) || navigator.language || '';
    const lang = raw.toLowerCase();
    if (lang.startsWith('es')) return 'es';
    if (lang.startsWith('en')) return 'en';
    return 'pt-BR';
  }

  function toShortLang(lang) {
    if (lang === 'pt-BR' || lang === 'pt') return 'pt';
    if (lang === 'en') return 'en';
    if (lang === 'es') return 'es';
    return 'pt';
  }

  function languageHref(langCode) {
    const short = toShortLang(langCode);
    return `${basePath}${CONFIG[short].path || ''}` || './';
  }

  function maybeRedirectToPreferredLanguage() {
    if (!shouldAutodetect) return;
    const params = new URLSearchParams(window.location.search);
    const forced = params.get('lang');
    const stored = localStorage.getItem('aiMaturityLang');
    const target = forced || stored || detectBrowserLanguage();
    if (target && target !== pageLang) {
      window.location.replace(languageHref(target));
    }
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function resolveAsset(path) {
    if (/^https?:\/\//.test(path)) return path;
    return `${basePath}${path}`;
  }

  function logoSvg(label, title) {
    return `<svg viewBox="0 0 1914 1062" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${escapeHtml(label)}"><title>${escapeHtml(title)}</title>${LOGO_PATHS}</svg>`;
  }

  function renderLanguageLinks(currentLang) {
    return Object.values(CONFIG).map((language) => {
      if (language.code === currentLang) {
        return `<strong>${language.label}</strong>`;
      }
      return `<a href="${languageHref(language.code)}" data-lang-choice="${language.code}">${language.label}</a>`;
    }).join(' · ');
  }

  function renderChrome(content) {
    const navItems = Object.entries(content.nav).map(([id, label]) => `<a href="#${id}">${escapeHtml(label)}</a>`).join('');
    return `
      <div class="chrome">
        <div class="chrome__inner">
          <div class="chrome__brand">
            ${logoSvg('paulasilva', 'paulasilva')}
            <div class="chrome__brand-text">${escapeHtml(content.brand.name)}<br>${escapeHtml(content.brand.role)}</div>
          </div>
          <nav class="chrome__nav" aria-label="Primary navigation">
            ${navItems}
            <span class="chrome__lang" aria-label="Language selector">${renderLanguageLinks(pageLang)}</span>
          </nav>
        </div>
      </div>`;
  }

  function renderHero(content) {
    const rows = content.hero.cardRows.map((row) => `
      <div class="hero__card-row">
        <div class="hero__card-icon hero__card-icon--${escapeHtml(row.iconClass)}">${escapeHtml(row.icon)}</div>
        <div><strong>${escapeHtml(row.title)}</strong><br><span class="hero__card-copy">${escapeHtml(row.subtitle)}</span></div>
        <span class="hero__card-num">${escapeHtml(row.metric)}</span>
      </div>`).join('');

    return `
      <section class="hero">
        <div class="hero__inner">
          <div>
            <div class="hero__eyebrow"><span class="hero__eyebrow-dot"></span>${escapeHtml(content.hero.eyebrow)}</div>
            <h1 class="hero__title">${escapeHtml(content.hero.titleBefore)} <span class="accent">${escapeHtml(content.hero.titleAccent)}</span>${content.hero.titleAfter ? ` ${escapeHtml(content.hero.titleAfter)}` : ''}</h1>
            <p class="hero__lede">${escapeHtml(content.hero.lede)}</p>
            <div class="hero__ctas">
              <a class="btn btn--primary" href="#download">${escapeHtml(content.hero.primaryCta)}</a>
              <a class="btn btn--secondary" href="#quickstart">${escapeHtml(content.hero.secondaryCta)}</a>
            </div>
          </div>
          <aside class="hero__card">
            <div class="hero__card-title">${escapeHtml(content.hero.cardTitle)}</div>
            <div class="hero__card-rows">${rows}</div>
          </aside>
        </div>
      </section>`;
  }

  function renderPipeline(content) {
    const steps = content.pipeline.steps.map((step) => `
      <div class="pipe-step pipe-step--${escapeHtml(step.kind)}">
        <div class="pipe-step__num">${escapeHtml(step.num)}</div>
        <div class="pipe-step__name">${escapeHtml(step.name)}</div>
        <div class="pipe-step__hint">${escapeHtml(step.hint)}</div>
      </div>`).join('');
    return `
      <section class="pipeline" id="pipeline">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.pipeline.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.pipeline.title)}</h2>
          <p class="section__lede">${escapeHtml(content.pipeline.lede)}</p>
          <div class="pipeline__chain">${steps}</div>
        </div>
      </section>`;
  }

  function renderSurveys(content) {
    const cards = content.surveys.cards.map((card) => {
      const meta = card.meta.map((item) => `<div><strong>${escapeHtml(item.value)}</strong>${escapeHtml(item.label)}</div>`).join('');
      const list = card.items.map((item) => `<li>${escapeHtml(item)}</li>`).join('');
      return `
        <article class="card card--${escapeHtml(card.variant)}">
          <div class="card__badge"><span class="card__badge-dot"></span>${escapeHtml(card.badge)}</div>
          <h3 class="card__title">${escapeHtml(card.title)}</h3>
          <div class="card__subtitle">${escapeHtml(card.subtitle)}</div>
          <div class="card__meta">${meta}</div>
          <ul class="card__list">${list}</ul>
        </article>`;
    }).join('');

    return `
      <section id="surveys">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.surveys.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.surveys.title)}</h2>
          <p class="section__lede">${escapeHtml(content.surveys.lede)}</p>
          <div class="cards">${cards}</div>
        </div>
      </section>`;
  }

  function renderQuickstart(content) {
    const steps = content.quickstart.steps.map((step) => `
      <div class="step">
        <div class="step__num">${escapeHtml(step.num)}</div>
        <h3 class="step__title">${escapeHtml(step.title)}</h3>
        <p class="step__body">${escapeHtml(step.body)}</p>
        <code class="step__cmd">${escapeHtml(step.command)}</code>
      </div>`).join('');
    return `
      <section id="quickstart" class="section--paper">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.quickstart.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.quickstart.title)}</h2>
          <p class="section__lede">${escapeHtml(content.quickstart.lede)}</p>
          <div class="steps">${steps}</div>
        </div>
      </section>`;
  }

  function renderSkills(content) {
    const skills = content.skills.items.map((skill) => `
      <div class="skill-pill"><div><div class="skill-pill__cmd">${escapeHtml(skill.cmd)}</div><div class="skill-pill__desc">${escapeHtml(skill.desc)}</div></div></div>`).join('');
    return `
      <section id="skills">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.skills.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.skills.title)}</h2>
          <p class="section__lede">${escapeHtml(content.skills.lede)}</p>
          <div class="skills-grid">${skills}</div>
        </div>
      </section>`;
  }

  function renderFaq(content) {
    const items = content.faq.items.map((item) => `
      <details class="faq__item">
        <summary>${escapeHtml(item.summary)}</summary>
        <p>${item.answerHtml}</p>
      </details>`).join('');
    return `
      <section id="faq" class="section--paper section--faq">
        <div class="container faq-container">
          <div class="section__eyebrow">${escapeHtml(content.faq.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.faq.title)}</h2>
          <p class="section__lede">${escapeHtml(content.faq.lede)}</p>
          <div class="faq">${items}</div>
        </div>
      </section>`;
  }

  function renderDownload(content, data) {
    const shortLang = toShortLang(pageLang);
    const downloadUrl = resolveAsset(data.downloads[pageLang] || data.downloads[shortLang] || data.downloads['pt-BR']);
    const panelItems = content.download.panelItems.map((item) => `<li>${escapeHtml(item.label)}<code>${escapeHtml(item.code)}</code></li>`).join('');
    return `
      <section class="download" id="download">
        <div class="container">
          <div class="download__inner">
            <div>
              <div class="section__eyebrow">${escapeHtml(content.download.eyebrow)}</div>
              <h2 class="section__title">${escapeHtml(content.download.title)}</h2>
              <p class="section__lede">${escapeHtml(content.download.lede)}</p>
              <div class="download__cta">
                <a class="btn btn--primary" href="${escapeHtml(downloadUrl)}">${escapeHtml(content.download.primaryCta)}</a>
                <a class="btn btn--secondary download__repo" href="${escapeHtml(data.repositoryUrl)}">${escapeHtml(content.download.secondaryCta)}</a>
              </div>
              <p class="download__hint">${escapeHtml(content.download.hintPrefix)} <code class="download__clone">${escapeHtml(content.download.cloneCommand)}</code></p>
            </div>
            <div class="download__panel">
              <div class="download__panel-title">${escapeHtml(content.download.panelTitle)}</div>
              <ul>${panelItems}</ul>
            </div>
          </div>
        </div>
      </section>`;
  }

  function renderFooter(content, data) {
    return `
      <footer class="footer">
        <div class="footer__inner">
          <div class="footer__sig">
            ${logoSvg('paulasilva', 'paulasilva')}
            <div class="footer__sig-text">
              <div class="footer__sig-name">${escapeHtml(content.brand.name)}</div>
              <div class="footer__sig-role">${escapeHtml(content.brand.role)}</div>
            </div>
          </div>
          <div class="footer__contact">
            <a href="mailto:${escapeHtml(data.contactEmail)}">${escapeHtml(data.contactEmail)}</a><br>
            <span class="footer__tagline">${escapeHtml(content.brand.tagline)}</span>
          </div>
        </div>
      </footer>`;
  }

  function render(content, data) {
    document.documentElement.lang = content.htmlLang;
    document.title = content.title;
    const description = document.querySelector('meta[name="description"]');
    if (description) description.setAttribute('content', content.description);

    app.innerHTML = [
      renderChrome(content),
      '<main id="main">',
      renderHero(content),
      renderPipeline(content),
      renderSurveys(content),
      renderQuickstart(content),
      renderSkills(content),
      renderFaq(content),
      renderDownload(content, data),
      '</main>',
      renderFooter(content, data)
    ].join('');

    document.querySelectorAll('[data-lang-choice]').forEach((link) => {
      link.addEventListener('click', () => localStorage.setItem('aiMaturityLang', link.dataset.langChoice));
    });
  }

  function renderLoadError() {
    app.innerHTML = `
      <main class="loading loading--error">
        <h1>AI Maturity Assessment Kit</h1>
        <p>Unable to load <code>${escapeHtml(contentPath)}</code>. For local preview, run <code>cd docs && python3 -m http.server 8000</code> and open <code>http://localhost:8000</code>.</p>
      </main>`;
  }

  async function boot() {
    maybeRedirectToPreferredLanguage();
    try {
      const response = await fetch(contentPath, { cache: 'no-cache' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      const content = data.i18n[pageLang] || data.i18n['pt-BR'];
      render(content, data);
    } catch (error) {
      console.error(error);
      renderLoadError();
    }
  }

  boot();
})();
