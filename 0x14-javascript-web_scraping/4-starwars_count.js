#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present

const ID = '18/';
const apiUrl = process.argv[2];
const request = require('request');

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const results = jsonBody.results;
    let num = 0;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        const charsID = characters[j].endsWith(ID);
        if (charsID) {
          num++;
        }
      }
    }
    console.log(num);
  }
});
