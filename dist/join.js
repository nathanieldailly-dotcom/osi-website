document.querySelectorAll('.join-form').forEach(form => {
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const fields = new FormData(form);
    const body = `Name: ${fields.get('Name')}\nEmail: ${fields.get('Email')}\n\nWhat I’d like to do:\n${fields.get('Interest')}`;
    const destination = `mailto:${form.dataset.joinEmail}?subject=${encodeURIComponent('Join OSI — Volunteer application')}&body=${encodeURIComponent(body)}`;
    window.location.href = destination;
    const status = form.querySelector('.join-form-status');
    status.hidden = false;
    status.textContent = 'Your application is ready in your email app. Please send it there to reach OSI.';
  });
});
