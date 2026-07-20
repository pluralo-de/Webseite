// Scroll reveal
  const revealEls = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.15 });
  revealEls.forEach(el=>io.observe(el));

  // Impressum / Datenschutz toggle boxes
  function setupToggleBox(linkEl, boxEl){
    if(!linkEl || !boxEl) return;
    linkEl.addEventListener('click', (e)=>{
      e.preventDefault();
      boxEl.classList.toggle('show');
      if(boxEl.classList.contains('show')){
        boxEl.scrollIntoView({behavior:'smooth', block:'start'});
      }
    });
  }
  const impressumBox = document.getElementById('impressumBox');
  const datenschutzBox = document.getElementById('datenschutzBox');
  setupToggleBox(document.getElementById('impressumLink'), impressumBox);
  setupToggleBox(document.getElementById('datenschutzLink'), datenschutzBox);
  setupToggleBox(document.getElementById('datenschutzLinkInline'), datenschutzBox);

  // Contact form validation + simulated submit
  const form = document.getElementById('contactForm');
  const successMsg = document.getElementById('formSuccess');

  function validateField(field, condition){
    field.classList.toggle('invalid', !condition);
    return condition;
  }

  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const subject = document.getElementById('subject');
    const message = document.getElementById('message');
    const consent = document.getElementById('consent');

    const nameOk = validateField(name.closest('.field'), name.value.trim().length > 1);
    const emailOk = validateField(email.closest('.field'), /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim()));
    const subjectOk = validateField(subject.closest('.field'), subject.value.trim().length > 1);
    const msgOk = validateField(message.closest('.field'), message.value.trim().length > 5);
    const consentOk = validateField(consent.closest('.field'), consent.checked);

    if(nameOk && emailOk && subjectOk && msgOk && consentOk){
      sendMail(name.value, email.value, document.getElementById('company').value, subject.value, message.value);
    }
  });

  // Mobile menu (simple: scroll to nav links via alert-free fallback)
  const burgerBtn = document.getElementById('burgerBtn');
  let mobileOpen = false;
  burgerBtn.addEventListener('click', ()=>{
    mobileOpen = !mobileOpen;
    const navLinks = document.querySelector('.nav-links');
    if(mobileOpen){
      navLinks.style.display = 'flex';
      navLinks.style.position = 'fixed';
      navLinks.style.top = '68px';
      navLinks.style.left = '0';
      navLinks.style.right = '0';
      navLinks.style.background = '#06090b';
      navLinks.style.flexDirection = 'column';
      navLinks.style.padding = '24px 32px';
      navLinks.style.borderBottom = '1px solid var(--ink-line)';
      navLinks.style.gap = '18px';
    } else {
      navLinks.removeAttribute('style');
    }
  });
  document.querySelectorAll('.nav-links a').forEach(a=>{
    a.addEventListener('click', ()=>{
      if(mobileOpen){ mobileOpen=false; document.querySelector('.nav-links').removeAttribute('style'); }
    });
  });



  function sendMail(name, email, company, subject, message) {
    const submitBtn = form.querySelector('.form-submit');
    submitBtn.disabled = true;
    submitBtn.textContent = 'Wird gesendet...';

    const parms = {
      thema: subject,
      name: company ? `${name} (${company})` : name,
      email: email,
      Nachricht: message
    };

    emailjs.send('service_g3rut4d', 'template_8dy5zsq', parms).then(
      () => {
        form.classList.add('sent');
        successMsg.classList.add('show');
      },
      (error) => {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Nachricht senden';
        alert('Beim Senden ist ein Fehler aufgetreten: ' + JSON.stringify(error));
      }
    );
  }