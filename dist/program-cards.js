(() => {
  const cards = [...document.querySelectorAll('.service-card')];
  const fine = matchMedia('(hover: hover) and (pointer: fine)');
  cards.forEach(card => {
    card.addEventListener('pointerenter', event => {
      if (fine.matches && event.pointerType === 'mouse') card.open = true;
    });
    card.addEventListener('pointerleave', event => {
      if (fine.matches && event.pointerType === 'mouse' && !card.contains(document.activeElement)) card.open = false;
    });
    card.addEventListener('focusout', event => {
      if (!card.contains(event.relatedTarget) && !card.matches(':hover')) card.open = false;
    });
  });
})();
