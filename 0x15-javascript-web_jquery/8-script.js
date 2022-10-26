// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (swapi) {
  for (let i = 0; i < swapi.results.length; i++) {
    $('UL#list_movies').append('<li>' + swapi.results[i].title + '</li>');
  }
});
