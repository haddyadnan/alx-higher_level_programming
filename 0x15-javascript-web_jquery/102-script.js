// Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
// Script must work when imported from <head> tag

const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const LangCode = $('INPUT#language_code').val();

    $.get('https://stefanbohacek.com/hellosalut/?lang=' + LangCode, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
