#!/usr/bin/node

const request = require('request');
const ID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + ID;

request(url, function (error, response, body) {
  if (error) {
    console.log('error');
  } else {
    const characters = JSON.parse(body).characters;
    const temp = [];
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
          temp.push(JSON.parse(body).name);
        }
      });
    }
    console.log(temp);
  }
});
