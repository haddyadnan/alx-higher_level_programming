#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const jsonBody = JSON.parse(body);
    for (let i = 0; i < jsonBody.length; i++) {
      if (jsonBody[i].completed) {
        const userId = jsonBody[i].userId;
        if (dict[userId]) {
          dict[userId]++;
        } else {
          dict[userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
