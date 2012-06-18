;(function($) {
  $(function() {
    $('iframe.html-page-preview').each(function() {
      var $frame = $(this);
      var $doc = $frame.contents();
      $doc.ready(function() { $frame.height($doc.find('html').height()); });
    });
  });
})(jQuery);
