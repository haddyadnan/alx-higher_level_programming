// Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header

const $ = window.$;
$('DIV#toggle_header').on('click', function () {
  $('header').toggleClass('red green');
});
