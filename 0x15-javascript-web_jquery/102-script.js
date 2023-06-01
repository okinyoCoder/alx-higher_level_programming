$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const resp = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang={resp}', function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
