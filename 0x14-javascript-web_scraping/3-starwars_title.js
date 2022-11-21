#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

const movieID = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else { console.log(JSON.parse(body).title); }
});
