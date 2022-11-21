#!/usr/bin/node
// A script that writes a string to a file

const fPath = process.argv[2];
const stringArg = process.argv[3];
const fs = require('fs');

fs.writeFile(fPath, stringArg, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
