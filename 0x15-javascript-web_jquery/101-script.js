// Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks
// Must run when loaded from head tag
const $ = window.$;

$(document).ready(function () {
  $('div#add_item').on('click', function () {
    $('ul.my_list').append('<LI>Item</LI>');
  });

  $('div#remove_item').on('click', function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', function () {
    $('ul.my_list').empty();
  });
});
