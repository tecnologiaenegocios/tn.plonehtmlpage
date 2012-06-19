;(function($) {
  $(function() {
    $('iframe.html-page-preview').each(function() {
      var $frame = $(this);
      var $doc = $frame.contents();
      var heightFn = function() { $frame.height($doc.find('html').height()); }
      $doc.load(heightFn);
      $doc.ready(heightFn);
    });
  });
})(jQuery);
