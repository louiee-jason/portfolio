

document.addEventListener('DOMContentLoaded', () => {

  const preloader = document.getElementById('preloader');
  window.addEventListener('load', () => {
    setTimeout(() => preloader.classList.add('hidden'), 800);
  });

  setTimeout(() => preloader.classList.add('hidden'), 3000);

  const canvas = document.getElementById('particles-canvas');
  const ctx = canvas.getContext('2d');
  let particles = [];
  let animationId;
  let mouseX = -1000;
  let mouseY = -1000;

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  class Particle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 1.5 + 0.3;
      this.speedX = (Math.random() - 0.5) * 0.25;
      this.speedY = (Math.random() - 0.5) * 0.25;
      this.opacity = Math.random() * 0.2 + 0.05;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;

      const dx = this.x - mouseX;
      const dy = this.y - mouseY;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 120) {
        const force = (120 - dist) / 120;
        this.x += (dx / dist) * force * 1.5;
        this.y += (dy / dist) * force * 1.5;
      }

      if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
      if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(176, 137, 104, ${this.opacity})`;
      ctx.fill();
    }
  }

  function initParticles() {
    const count = Math.min(Math.floor((canvas.width * canvas.height) / 18000), 80);
    particles = [];
    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }

  function connectParticles() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 140) {
          const opacity = (1 - dist / 140) * 0.06;
          ctx.beginPath();
          ctx.strokeStyle = `rgba(176, 137, 104, ${opacity})`;
          ctx.lineWidth = 0.6;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
  }

  function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    connectParticles();
    animationId = requestAnimationFrame(animateParticles);
  }

  initParticles();
  animateParticles();
  window.addEventListener('resize', () => {
    cancelAnimationFrame(animationId);
    initParticles();
    animateParticles();
  });

  const typingEl = document.getElementById('typingText');
  const phrases = [
    'Electrical Engineering Student',
    'AI & Automation Enthusiast',
    'Robotics & Data Science',
    'Machine Learning Developer',
    'IoT Systems Builder'
  ];
  let phraseIdx = 0;
  let charIdx = 0;
  let isDeleting = false;
  let typeSpeed = 80;

  function typeEffect() {
    const current = phrases[phraseIdx];
    if (isDeleting) {
      typingEl.textContent = current.substring(0, charIdx - 1);
      charIdx--;
      typeSpeed = 40;
    } else {
      typingEl.textContent = current.substring(0, charIdx + 1);
      charIdx++;
      typeSpeed = 80;
    }

    if (!isDeleting && charIdx === current.length) {
      typeSpeed = 2000; // pause at end
      isDeleting = true;
    } else if (isDeleting && charIdx === 0) {
      isDeleting = false;
      phraseIdx = (phraseIdx + 1) % phrases.length;
      typeSpeed = 400; // pause before next phrase
    }

    setTimeout(typeEffect, typeSpeed);
  }
  typeEffect();

  const navbar = document.getElementById('navbar');
  const navLinksContainer = document.getElementById('navLinks');
  const navLinks = navLinksContainer.querySelectorAll('a');
  const sections = document.querySelectorAll('section[id]');

  function updateNavbar() {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    let current = '';
    sections.forEach(section => {
      const top = section.offsetTop - 120;
      if (window.scrollY >= top) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', updateNavbar);
  updateNavbar();

  const hamburger = document.getElementById('hamburger');
  const navOverlay = document.getElementById('navOverlay');

  function toggleMenu() {
    hamburger.classList.toggle('active');
    navLinksContainer.classList.toggle('open');
    navOverlay.classList.toggle('visible');
    document.body.style.overflow = navLinksContainer.classList.contains('open') ? 'hidden' : '';
  }

  hamburger.addEventListener('click', toggleMenu);
  navOverlay.addEventListener('click', toggleMenu);

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navLinksContainer.classList.contains('open')) {
        toggleMenu();
      }
    });
  });

  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;

      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      tabContents.forEach(tc => {
        tc.classList.remove('active');
        if (tc.id === target) {
          tc.classList.add('active');

          tc.querySelectorAll('.reveal').forEach(el => {
            el.classList.remove('revealed');
            setTimeout(() => revealCheck(el), 50);
          });
        }
      });
    });
  });

  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');

  function revealCheck(el) {
    const rect = el.getBoundingClientRect();
    const windowH = window.innerHeight;
    if (rect.top < windowH - 80) {
      el.classList.add('revealed');
    }
  }

  function onScrollReveal() {
    revealElements.forEach(el => revealCheck(el));
  }

  window.addEventListener('scroll', onScrollReveal);

  setTimeout(onScrollReveal, 100);

  const scrollTopBtn = document.getElementById('scrollTopBtn');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      scrollTopBtn.classList.add('visible');
    } else {
      scrollTopBtn.classList.remove('visible');
    }
  });

  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  const contactForm = document.getElementById('contactForm');

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = contactForm.querySelector('.form-submit-btn');
    const originalText = btn.innerHTML;

    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
    btn.disabled = true;

    try {
      const response = await fetch(contactForm.action, {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        btn.innerHTML = '<i class="fa-solid fa-check"></i> Message Sent!';
        btn.style.background = '#4ade80';
        contactForm.reset();
      } else {
        btn.innerHTML = '<i class="fa-solid fa-xmark"></i> Failed — Try Again';
        btn.style.background = '#f87171';
      }
    } catch (err) {
      btn.innerHTML = '<i class="fa-solid fa-xmark"></i> Network Error';
      btn.style.background = '#f87171';
    }

    setTimeout(() => {
      btn.innerHTML = originalText;
      btn.style.background = '';
      btn.disabled = false;
    }, 3000);
  });

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  const cvDropdownBtn = document.getElementById('cvDropdownBtn');
  const cvDropdownMenu = document.getElementById('cvDropdownMenu');

  if (cvDropdownBtn && cvDropdownMenu) {
    cvDropdownBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      cvDropdownMenu.classList.toggle('show');
    });

    document.addEventListener('click', (e) => {
      if (!cvDropdownMenu.contains(e.target) && e.target !== cvDropdownBtn) {
        cvDropdownMenu.classList.remove('show');
      }
    });
  }

});
