#!/usr/bin/node
// a script that reads and prints the content of a file.

const fPath = process.argv[2];
const fs = require('fs');

fs.readFile(fPath, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
