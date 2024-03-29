#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:

const request = require('request');
const ID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + ID;

request(url, function (error, response, body) {
  if (error) {
    console.log('error');
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, chars) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(chars).name);
        }
      });
    }
  }
});
