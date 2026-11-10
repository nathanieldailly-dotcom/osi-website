// Section slides complement the mission’s existing pop animation.
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const sections = [...document.querySelectorAll('main > section:not(#home):not(#mission) > .wrap')];
  let observer;
  function sync() {
    observer?.disconnect();
    sections.forEach(section => section.classList.remove('section-slide', 'section-in'));
    if (reduced.matches || !('IntersectionObserver' in window)) return;
    observer = new IntersectionObserver(entries => {
      entries.forEach(entry => entry.target.classList.toggle('section-in', entry.isIntersecting));
    }, {threshold: .08, rootMargin: '0px 0px -35px 0px'});
    sections.forEach((section, index) => {
      section.classList.add('section-slide');
      section.style.setProperty('--section-slide-x', index % 2 ? '28px' : '-28px');
      observer.observe(section);
    });
  }
  sync();
  reduced.addEventListener('change', sync);
})();

// A soft white glow follows the native pointer, matching the supplied reference.
(() => {
  const fine = matchMedia('(hover: hover) and (pointer: fine)');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const glow = document.createElement('span');
  glow.className = 'cursor-glow';
  glow.setAttribute('aria-hidden', 'true');
  document.body.append(glow);
  let x = 0, y = 0, currentX = 0, currentY = 0, frame = 0, initialized = false;
  function hide() {
    glow.classList.remove('is-visible', 'is-interactive');
    cancelAnimationFrame(frame); frame = 0; initialized = false;
  }
  function move() {
    currentX += (x - currentX) * .24;
    currentY += (y - currentY) * .24;
    glow.style.transform = `translate3d(${currentX}px, ${currentY}px, 0)`;
    if (Math.abs(x - currentX) + Math.abs(y - currentY) > .15) frame = requestAnimationFrame(move);
    else { glow.style.transform = `translate3d(${x}px, ${y}px, 0)`; frame = 0; }
  }
  document.addEventListener('pointermove', event => {
    if (!fine.matches || reduced.matches || event.pointerType !== 'mouse' || event.target.closest('input,textarea,[contenteditable="true"]')) { hide(); return; }
    x = event.clientX; y = event.clientY;
    if (!initialized) { currentX = x; currentY = y; initialized = true; glow.style.transform = `translate3d(${x}px, ${y}px, 0)`; }
    glow.classList.add('is-visible');
    glow.classList.toggle('is-interactive', Boolean(event.target.closest('a,button,summary,[role="button"]')));
    if (!frame) frame = requestAnimationFrame(move);
  }, {passive:true});
  document.documentElement.addEventListener('pointerleave', hide);
  window.addEventListener('blur', hide);
  document.addEventListener('visibilitychange', () => { if (document.hidden) hide(); });
  document.addEventListener('keydown', event => { if (event.key === 'Tab') hide(); });
  fine.addEventListener('change', hide);
  reduced.addEventListener('change', hide);
})();
