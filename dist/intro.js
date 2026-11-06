(() => {
  const root = document.documentElement;
  const loader = document.querySelector('#site-loader');
  if (!loader) return;
  if (!root.classList.contains('site-starting')) {
    loader.remove();
    return;
  }
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const started = performance.now();
  const progress = loader.querySelector('progress');
  const hiddenContent = [...document.querySelectorAll('body > .skip-link, body > header, body > main, body > footer')].filter(element => !element.inert);
  hiddenContent.forEach(element => {
    element.inert = true;
    element.setAttribute('data-intro-inert', '');
  });
  let finished = false;
  function finish() {
    if (finished) return;
    finished = true;
    const returnFocus = loader.contains(document.activeElement);
    hiddenContent.forEach(element => {
      element.inert = false;
      element.removeAttribute('data-intro-inert');
    });
    if (progress) progress.value = 100;
    loader.classList.add('is-leaving');
    document.removeEventListener('keydown', onKey);
    setTimeout(() => {
      root.classList.remove('site-starting');
      loader.remove();
      // Restore deep links after releasing the loading screen's scroll lock.
      if (location.hash) {
        let target;
        try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch {}
        target?.scrollIntoView({behavior:'instant', block:'start'});
      }
      if (returnFocus) document.querySelector('#main')?.focus({preventScroll:true});
    }, reducedMotion ? 0 : 350);
  }
  function onKey(event) { if (event.key === 'Escape') finish(); }
  document.addEventListener('keydown', onKey);
  const images = [loader.querySelector('img'), document.querySelector('.hero-background-photo')].filter(Boolean);
  const tasks = images.map(image => image.decode ? image.decode() : Promise.resolve());
  if (document.fonts) tasks.push(document.fonts.ready);
  let loaded = 0;
  const ready = Promise.allSettled(tasks.map(task => Promise.resolve(task).finally(() => {
    loaded += 1;
    if (progress) progress.value = Math.round(loaded / tasks.length * 100);
  })));
  // Keep the welcome brief, even on slow connections.
  const maximum = setTimeout(finish, 2600);
  ready.then(() => {
    const minimum = 1200;
    setTimeout(() => { clearTimeout(maximum); finish(); }, Math.max(0, minimum - (performance.now() - started)));
  });
  window.addEventListener('pageshow', event => { if (event.persisted) finish(); });
})();
