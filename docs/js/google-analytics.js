//Based on:
//
//<!-- Google tag (gtag.js) -->
//<script async src="https://www.googletagmanager.com/gtag/js?id=G-35NN9PBX18"></script>
//<script>
//    window.dataLayer = window.dataLayer || [];
//    function gtag(){dataLayer.push(arguments);}
//    gtag('js', new Date());
//
//    gtag('config', 'G-35NN9PBX18');
//</script>

// google-analytics.js
(function () {
  // Load the Google Analytics script dynamically
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-35NN9PBX18';
  script.onload = function () {
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('config', 'G-35NN9PBX18');
  };
  document.head.appendChild(script);
})();
