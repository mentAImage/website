(function () {
  var path = window.location.pathname.replace(/\/index\.html$/, '/');

  // Pages that have a proper FR equivalent
  var enToFr = {
    '/': '/fr/',
    '/about.html': '/fr/about.html',
    '/contact.html': '/fr/contact.html',
    '/monai.html': '/fr/monai.html',
    '/pulsekey.html': '/fr/pulsekey.html',
    '/privacy.html': '/fr/privacy.html',
    '/terms.html': '/fr/terms.html',
    '/neurodiversity-at-work-stories/': '/fr/'
  };
  var frToEn = {};
  for (var k in enToFr) { frToEn[enToFr[k]] = k; }

  var langLinks = document.querySelectorAll('.nav__link--lang');

  if (path.startsWith('/fr/')) {
    // On a FR page — point EN link to EN equivalent
    var enPath = frToEn[path] || path.replace(/^\/fr/, '') || '/';
    langLinks.forEach(function (el) {
      if (el.textContent.trim() === 'EN') el.setAttribute('href', enPath);
    });
  } else {
    // On an EN page — point FR link to FR equivalent, or #francais for story pages
    var frPath = enToFr[path] || '#francais';
    langLinks.forEach(function (el) {
      if (el.textContent.trim() === 'FR') el.setAttribute('href', frPath);
    });
  }
})();
