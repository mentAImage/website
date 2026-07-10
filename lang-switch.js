(function () {
  var path = window.location.pathname.replace(/\/index\.html$/, '/');

  // EN pages that have a dedicated FR equivalent page
  var enToFr = {
    '/': '/fr/',
    '/about.html': '/fr/about.html',
    '/contact.html': '/fr/contact.html',
    '/monai.html': '/fr/monai.html',
    '/pulsekey.html': '/fr/pulsekey.html',
    '/privacy.html': '/fr/privacy.html',
    '/terms.html': '/fr/terms.html'
  };

  // FR → EN reverse map
  var frToEn = {};
  for (var k in enToFr) { frToEn[enToFr[k]] = k; }

  // All lang-switcher anchors (desktop + mobile)
  var langLinks = document.querySelectorAll('.nav__link--lang');

  if (path.startsWith('/fr/')) {
    // On a FR page: rewrite EN link to the EN equivalent
    var enPath = frToEn[path] || path.replace(/^\/fr/, '') || '/';
    langLinks.forEach(function (el) {
      el.setAttribute('href', enPath);
    });
  } else if (enToFr[path]) {
    // On an EN page with a real FR equivalent: go there
    langLinks.forEach(function (el) {
      el.setAttribute('href', enToFr[path]);
    });
  } else if (document.getElementById('francais')) {
    // On a bilingual story page: scroll to the French section
    langLinks.forEach(function (el) {
      el.setAttribute('href', '#francais');
    });
  } else {
    // English-only page (Stories index etc.): dim the FR button, don't navigate
    langLinks.forEach(function (el) {
      el.setAttribute('href', '#');
      el.style.opacity = '0.4';
      el.style.cursor = 'default';
      el.style.pointerEvents = 'none';
    });
  }
})();
