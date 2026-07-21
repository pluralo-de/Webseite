document.documentElement.classList.add('js');

const revealEls = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach((element) => observer.observe(element));
} else {
  revealEls.forEach((element) => element.classList.add('in'));
}

const legalBoxes = [
  document.getElementById('impressumBox'),
  document.getElementById('datenschutzBox')
].filter(Boolean);

function setToggleBoxState(boxElement, isOpen) {
  if (!boxElement) return;
  boxElement.classList.toggle('show', isOpen);
  document.querySelectorAll(`[aria-controls="${boxElement.id}"]`).forEach((link) => {
    link.setAttribute('aria-expanded', String(isOpen));
  });
}

function setupToggleBox(linkElement, boxElement) {
  if (!linkElement || !boxElement) return;

  linkElement.setAttribute('aria-controls', boxElement.id);
  linkElement.setAttribute('aria-expanded', 'false');
  linkElement.addEventListener('click', (event) => {
    event.preventDefault();
    const isOpen = !boxElement.classList.contains('show');
    legalBoxes.forEach((box) => setToggleBoxState(box, box === boxElement && isOpen));

    if (isOpen) {
      boxElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
      boxElement.setAttribute('tabindex', '-1');
      boxElement.focus({ preventScroll: true });
    }
  });
}

const impressumBox = document.getElementById('impressumBox');
const datenschutzBox = document.getElementById('datenschutzBox');
setupToggleBox(document.getElementById('impressumLink'), impressumBox);
setupToggleBox(document.getElementById('datenschutzLink'), datenschutzBox);
setupToggleBox(document.getElementById('datenschutzLinkInline'), datenschutzBox);

function openLegalBoxFromHash() {
  const box = legalBoxes.find((element) => `#${element.id}` === window.location.hash);
  if (!box) return;
  legalBoxes.forEach((element) => setToggleBoxState(element, element === box));
}

openLegalBoxFromHash();
window.addEventListener('hashchange', openLegalBoxFromHash);

const form = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');

function setFieldValidity(field, isValid) {
  if (!field) return isValid;
  field.classList.toggle('invalid', !isValid);
  const control = field.querySelector('input, textarea');
  if (control) control.setAttribute('aria-invalid', String(!isValid));
  return isValid;
}

function setFormStatus(message, type = '') {
  if (!formStatus) return;
  formStatus.textContent = message;
  formStatus.className = 'form-status';
  if (type) formStatus.classList.add(type);
}

if (form) {
  form.querySelectorAll('input, textarea').forEach((control) => {
    control.addEventListener('input', () => {
      const field = control.closest('.field');
      if (field?.classList.contains('invalid')) setFieldValidity(field, control.checkValidity());
    });
  });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    setFormStatus('');

    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const company = document.getElementById('company');
    const subject = document.getElementById('subject');
    const message = document.getElementById('message');
    const consent = document.getElementById('consent');
    const website = document.getElementById('website');

    if (website?.value) {
      form.classList.add('sent');
      setFormStatus('Danke! Ihre Nachricht ist angekommen. Wir melden uns in Kürze.', 'success');
      return;
    }

    const checks = [
      setFieldValidity(name?.closest('.field'), Boolean(name && name.value.trim().length > 1)),
      setFieldValidity(email?.closest('.field'), Boolean(email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim()))),
      setFieldValidity(subject?.closest('.field'), Boolean(subject && subject.value.trim().length > 1)),
      setFieldValidity(message?.closest('.field'), Boolean(message && message.value.trim().length > 5)),
      setFieldValidity(consent?.closest('.field'), Boolean(consent?.checked))
    ];

    if (!checks.every(Boolean)) {
      setFormStatus('Bitte prüfen Sie die markierten Felder.', 'error');
      form.querySelector('.invalid input, .invalid textarea')?.focus();
      return;
    }

    await sendMail({
      name: name.value.trim(),
      email: email.value.trim(),
      company: company.value.trim(),
      subject: subject.value.trim(),
      message: message.value.trim()
    });
  });
}

const burgerBtn = document.getElementById('burgerBtn');
const primaryNav = document.getElementById('primaryNav');

function closeMobileMenu({ restoreFocus = false } = {}) {
  if (!burgerBtn || !primaryNav) return;
  primaryNav.classList.remove('open');
  document.body.classList.remove('menu-open');
  burgerBtn.setAttribute('aria-expanded', 'false');
  burgerBtn.setAttribute('aria-label', 'Menü öffnen');
  burgerBtn.querySelector('span').textContent = '☰';
  if (restoreFocus) burgerBtn.focus();
}

function openMobileMenu() {
  if (!burgerBtn || !primaryNav) return;
  primaryNav.classList.add('open');
  document.body.classList.add('menu-open');
  burgerBtn.setAttribute('aria-expanded', 'true');
  burgerBtn.setAttribute('aria-label', 'Menü schließen');
  burgerBtn.querySelector('span').textContent = '×';
  primaryNav.querySelector('a')?.focus();
}

burgerBtn?.addEventListener('click', () => {
  const isOpen = burgerBtn.getAttribute('aria-expanded') === 'true';
  if (isOpen) closeMobileMenu();
  else openMobileMenu();
});

primaryNav?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => closeMobileMenu());
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && burgerBtn?.getAttribute('aria-expanded') === 'true') {
    closeMobileMenu({ restoreFocus: true });
  }
});

window.addEventListener('resize', () => {
  if (window.innerWidth > 920) closeMobileMenu();
});

async function sendMail({ name, email, company, subject, message }) {
  const submitButton = form?.querySelector('.form-submit');
  if (!form || !submitButton) return;

  submitButton.disabled = true;
  submitButton.textContent = 'Wird gesendet …';
  setFormStatus('Ihre Nachricht wird gesendet.');

  const controller = new AbortController();
  const timeoutId = window.setTimeout(() => controller.abort(), 15000);

  try {
    const response = await fetch('https://api.emailjs.com/api/v1.0/email/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'omit',
      referrerPolicy: 'strict-origin-when-cross-origin',
      signal: controller.signal,
      body: JSON.stringify({
        service_id: 'service_g3rut4d',
        template_id: 'template_8dy5zsq',
        user_id: 'Cyey8UpF_6g3_3OEy',
        template_params: {
          thema: subject,
          name: company ? `${name} (${company})` : name,
          email,
          Nachricht: message
        }
      })
    });
    if (!response.ok) throw new Error(`EmailJS antwortete mit Status ${response.status}.`);

    form.classList.add('sent');
    setFormStatus('Danke! Ihre Nachricht ist angekommen. Wir melden uns in Kürze.', 'success');
  } catch (error) {
    console.error('Kontaktformular:', error);
    submitButton.disabled = false;
    submitButton.textContent = 'Nachricht senden';
    setFormStatus('Die Nachricht konnte gerade nicht gesendet werden. Bitte schreiben Sie uns direkt an kontakt@pluralo.de.', 'error');
  } finally {
    window.clearTimeout(timeoutId);
  }
}
