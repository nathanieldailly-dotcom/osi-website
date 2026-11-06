(() => {
  const section = document.querySelector('#mission');
  if (!section) return;
  const words = [...section.querySelectorAll('[data-mission]')];
  const details = [...section.querySelectorAll('.mission-detail')];
  function show(word) {
    const id = word.getAttribute('aria-controls');
    words.forEach(item => item.setAttribute('aria-pressed', String(item === word)));
    details.forEach(detail => {
      const active = detail.id === id;
      if (active && detail.hidden) {
        detail.classList.remove('is-changing');
        detail.hidden = false;
        detail.classList.add('is-changing');
      } else if (!active) detail.hidden = true;
    });
  }
  words.forEach(word => {
    word.addEventListener('pointerenter', event => { if (event.pointerType !== 'touch') show(word); });
    word.addEventListener('focus', () => show(word));
    word.addEventListener('click', () => show(word));
  });
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if ('IntersectionObserver' in window && !reduced.matches) {
    section.classList.add('mission-ready');
    const observer = new IntersectionObserver(entries => {
      if (!entries.some(entry => entry.isIntersecting)) return;
      section.classList.add('is-visible');
      observer.disconnect();
    }, {threshold: .16});
    observer.observe(section);
    reduced.addEventListener('change', () => {
      if (reduced.matches) { section.classList.add('is-visible'); observer.disconnect(); }
    });
  }
})();
