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

// Event filters use the documented service categories.
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
  const category = button.dataset.filter;
  document.querySelectorAll('[data-filter]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  document.querySelectorAll('[data-category]').forEach(event => { event.hidden = category !== 'all' && event.dataset.category !== category; });
}));
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
