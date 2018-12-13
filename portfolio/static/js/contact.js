$(function() {
    var $id_message = $('#id_message');
    var lineHeight = parseInt($id_message.css('lineHeight'));
    $id_message.on('input', function(e) {
      var lines = ($(this).val() + '\n').match(/\n/g).length;
      $(this).height(lineHeight * lines);
    });
  });