;(function($) {
  $(window).load(function() {
    $('iframe.html-page-preview').each(function() {
      var $frame = $(this);
      $frame.height($frame.contents().find('html').height());
    });
  });
})(jQuery);
