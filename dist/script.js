// All content remains visible when JavaScript or motion is unavailable.
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('arrived');
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: .1});
  document.querySelectorAll('.reveal').forEach(element => observer.observe(element));
}

// Event filters are available once their behavior is ready.
const eventFilters = document.querySelector('.event-filters');
if (eventFilters) {
  const buttons = [...eventFilters.querySelectorAll('[data-filter]')];
  const events = [...document.querySelectorAll('.directory-event[data-category]')];
  const status = document.querySelector('#event-count');
  buttons.forEach(button => button.addEventListener('click', () => {
    const category = button.dataset.filter;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    let visible = 0;
    events.forEach(event => {
      event.hidden = category !== 'all' && event.dataset.category !== category;
      if (!event.hidden) visible += 1;
    });
    status.textContent = `${visible} ${visible === 1 ? 'event' : 'events'} shown.`;
  }));
  eventFilters.hidden = false;
}

const siteHeader = document.querySelector('.site-header');
const updateHeader = () => siteHeader.classList.toggle('is-scrolled', window.scrollY > 40);
window.addEventListener('scroll', updateHeader, {passive: true});
updateHeader();

// The navigation becomes white while someone interacts with it.
siteHeader.addEventListener('pointerdown', () => siteHeader.classList.add('is-engaged'));
siteHeader.addEventListener('click', () => siteHeader.classList.add('is-engaged'));
siteHeader.addEventListener('focusin', () => siteHeader.classList.add('is-engaged'));
function resetHeaderWhenOutside(event) {
  if (!siteHeader.contains(event.target)) siteHeader.classList.remove('is-engaged');
}
document.addEventListener('pointerdown', resetHeaderWhenOutside);
document.addEventListener('click', resetHeaderWhenOutside);
document.addEventListener('focusin', resetHeaderWhenOutside);
