(function () {
  'use strict';

  // Mobile hamburger
  var hamburger = document.getElementById('hamburger');
  var mobileMenu = document.getElementById('mobile-menu');

  function closeMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.remove('open');
    mobileMenu.setAttribute('aria-hidden', 'true');
    if (hamburger) hamburger.setAttribute('aria-expanded', 'false');
  }

  if (hamburger) {
    hamburger.addEventListener('click', function () {
      var isOpen = mobileMenu.classList.toggle('open');
      mobileMenu.setAttribute('aria-hidden', String(!isOpen));
      hamburger.setAttribute('aria-expanded', String(isOpen));
    });
  }

  // Modal system
  function openModal(id) {
    var overlay = document.getElementById(id);
    if (!overlay) return;
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    var focusable = overlay.querySelectorAll('button, a, input, [tabindex]:not([tabindex="-1"])');
    if (focusable.length) focusable[0].focus();
  }

  function closeModal(id) {
    var overlay = document.getElementById(id);
    if (!overlay) return;
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  // Disclaimer triggers
  document.querySelectorAll('.disclaimer-trigger').forEach(function (btn) {
    btn.addEventListener('click', function () { openModal('modal-disclaimer'); });
  });

  // Close buttons inside modals
  document.querySelectorAll('[data-close]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      closeModal(btn.dataset.close);
    });
  });

  // Close on overlay background click
  document.querySelectorAll('.modal-overlay').forEach(function (overlay) {
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal(overlay.id);
    });
  });

  // Close on Escape key, trap focus inside modal
  document.addEventListener('keydown', function (e) {
    var openOverlay = document.querySelector('.modal-overlay.open');
    if (!openOverlay) return;

    if (e.key === 'Escape') {
      closeModal(openOverlay.id);
      return;
    }

    if (e.key === 'Tab') {
      var focusable = Array.from(openOverlay.querySelectorAll(
        'button:not([disabled]), a[href], input:not([disabled]), [tabindex]:not([tabindex="-1"])'
      ));
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) {
          e.preventDefault();
          last.focus();
        }
      } else {
        if (document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    }
  });

  // Nav shadow on scroll
  window.addEventListener('scroll', function () {
    var nav = document.querySelector('.nav');
    if (nav) {
      nav.style.boxShadow = window.scrollY > 8
        ? '0 1px 12px rgba(26,46,68,0.08)'
        : 'none';
    }
  }, { passive: true });

  // Contact form validation
  window.handleContactForm = function (e) {
    var form = e.target;
    var valid = true;
    form.querySelectorAll('[required]').forEach(function (field) {
      if (!field.value.trim()) {
        field.style.borderColor = '#c0392b';
        valid = false;
      } else {
        field.style.borderColor = '';
      }
    });
    if (!valid) { e.preventDefault(); return; }
    var submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Sending…'; }
  };

  // Contact success banner: show if ?sent=1
  (function () {
    var params = new URLSearchParams(window.location.search);
    if (params.get('sent') === '1') {
      var banner = document.getElementById('contact-success-banner');
      if (banner) banner.style.display = 'block';
    }
  })();

})();
