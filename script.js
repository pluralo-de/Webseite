'use strict';

const EMAILJS_PUBLIC_KEY = 'Cyey8UpF_6g3_3OEy';
const EMAILJS_SERVICE_ID = 'service_g3rut4d';
const EMAILJS_TEMPLATE_ID = 'template_8dy5zsq';

if (window.emailjs) {
  window.emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
}

// Hell- und Dunkelmodus umschalten und die Auswahl auf diesem Gerät merken.
const themeToggle = document.getElementById('themeToggle');
const themeColor = document.getElementById('themeColor');
const root = document.documentElement;

function getCurrentTheme() {
  return root.dataset.theme === 'light' ? 'light' : 'dark';
}

function updateThemeControls() {
  const isLight = getCurrentTheme() === 'light';

  if (themeToggle) {
    themeToggle.setAttribute('aria-checked', String(isLight));
    themeToggle.setAttribute('aria-label', isLight ? 'Dunkelmodus aktivieren' : 'Hellmodus aktivieren');
    themeToggle.title = isLight ? 'Dunkelmodus' : 'Hellmodus';
  }

  if (themeColor) {
    themeColor.setAttribute('content', isLight ? '#f4f8f7' : '#06090b');
  }
}

function setTheme(theme) {
  root.dataset.theme = theme;

  try {
    localStorage.setItem('pluralo-theme', theme);
  } catch (_) {
    // Der Schalter funktioniert auch, wenn lokaler Speicher blockiert ist.
  }

  updateThemeControls();
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    setTheme(getCurrentTheme() === 'dark' ? 'light' : 'dark');
  });
}

updateThemeControls();

// Elemente beim Scrollen einblenden.
const revealEls = document.querySelectorAll('.reveal');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  revealEls.forEach((element) => observer.observe(element));
} else {
  revealEls.forEach((element) => element.classList.add('in'));
}

// Impressum und Datenschutz öffnen; dabei bleibt immer nur eine Box sichtbar.
const impressumBox = document.getElementById('impressumBox');
const datenschutzBox = document.getElementById('datenschutzBox');
const legalBoxes = [impressumBox, datenschutzBox].filter(Boolean);

const legalTriggers = [
  { trigger: document.getElementById('impressumLink'), box: impressumBox },
  { trigger: document.getElementById('datenschutzLink'), box: datenschutzBox },
  { trigger: document.getElementById('datenschutzLinkInline'), box: datenschutzBox }
].filter(({ trigger, box }) => trigger && box);

function syncLegalTriggerStates() {
  legalTriggers.forEach(({ trigger, box }) => {
    trigger.setAttribute('aria-expanded', String(box.classList.contains('show')));
  });
}

function toggleLegalBox(box) {
  const shouldOpen = !box.classList.contains('show');
  legalBoxes.forEach((legalBox) => legalBox.classList.remove('show'));

  if (shouldOpen) {
    box.classList.add('show');
    box.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  syncLegalTriggerStates();
}

legalTriggers.forEach(({ trigger, box }) => {
  trigger.setAttribute('aria-controls', box.id);
  trigger.addEventListener('click', (event) => {
    event.preventDefault();
    toggleLegalBox(box);
  });
});

syncLegalTriggerStates();

if (window.location.hash === '#impressumBox' && impressumBox) {
  impressumBox.classList.add('show');
} else if (window.location.hash === '#datenschutzBox' && datenschutzBox) {
  datenschutzBox.classList.add('show');
}
syncLegalTriggerStates();

// Mobiles Menü.
const burgerBtn = document.getElementById('burgerBtn');
const navLinks = document.getElementById('mainNav');
let mobileOpen = false;

function setMobileMenu(open) {
  if (!burgerBtn || !navLinks) return;

  mobileOpen = open;
  navLinks.classList.toggle('is-open', open);
  document.body.classList.toggle('menu-open', open);
  burgerBtn.setAttribute('aria-expanded', String(open));
  burgerBtn.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
  burgerBtn.textContent = open ? '×' : '☰';
}

if (burgerBtn && navLinks) {
  burgerBtn.addEventListener('click', () => setMobileMenu(!mobileOpen));

  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setMobileMenu(false));
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && mobileOpen) {
      setMobileMenu(false);
      burgerBtn.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 1040 && mobileOpen) {
      setMobileMenu(false);
    }
  });
}

// Kontaktformular validieren und über EmailJS senden.
const form = document.getElementById('contactForm');
const successMsg = document.getElementById('formSuccess');
const errorMsg = document.getElementById('formError');

function validateField(control, condition) {
  const field = control.closest('.field');
  if (!field) return condition;

  field.classList.toggle('invalid', !condition);
  control.setAttribute('aria-invalid', String(!condition));
  return condition;
}

function clearFormMessage() {
  if (!errorMsg) return;
  errorMsg.hidden = true;
  errorMsg.textContent = '';
}

function showFormError(message) {
  if (!errorMsg) return;
  errorMsg.textContent = message;
  errorMsg.hidden = false;
}

function showFormSuccess() {
  form.classList.add('sent');
  clearFormMessage();
  successMsg?.classList.add('show');
}

async function sendMail(name, email, company, subject, message) {
  const submitBtn = form.querySelector('.form-submit');
  submitBtn.disabled = true;
  submitBtn.textContent = 'Wird gesendet…';

  const params = {
    thema: subject,
    name: company ? `${name} (${company})` : name,
    email,
    Nachricht: message
  };

  try {
    if (!window.emailjs) {
      throw new Error('EmailJS konnte nicht geladen werden.');
    }

    await window.emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, params);
    showFormSuccess();
    form.reset();
  } catch (error) {
    console.error('Kontaktformular konnte nicht gesendet werden.', error);
    showFormError('Das Senden hat leider nicht funktioniert. Bitte versuchen Sie es erneut oder schreiben Sie direkt an pluralo.allg@gmail.com.');
    submitBtn.disabled = false;
    submitBtn.textContent = 'Nachricht senden';
  }
}

if (form) {
  form.querySelectorAll('input, textarea').forEach((control) => {
    const eventName = control.type === 'checkbox' ? 'change' : 'input';
    control.addEventListener(eventName, () => {
      control.closest('.field')?.classList.remove('invalid');
      control.removeAttribute('aria-invalid');
      clearFormMessage();
    });
  });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    clearFormMessage();

    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const company = document.getElementById('company');
    const subject = document.getElementById('subject');
    const message = document.getElementById('message');
    const consent = document.getElementById('consent');
    const website = document.getElementById('website');

    const checks = [
      validateField(name, name.value.trim().length > 1),
      validateField(email, /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())),
      validateField(subject, subject.value.trim().length > 1),
      validateField(message, message.value.trim().length > 5),
      validateField(consent, consent.checked)
    ];

    if (!checks.every(Boolean)) {
      form.querySelector('[aria-invalid="true"]')?.focus();
      return;
    }

    // Bots füllen dieses unsichtbare Feld häufig aus.
    if (website.value.trim()) {
      showFormSuccess();
      return;
    }

    await sendMail(
      name.value.trim(),
      email.value.trim(),
      company.value.trim(),
      subject.value.trim(),
      message.value.trim()
    );
  });
}
