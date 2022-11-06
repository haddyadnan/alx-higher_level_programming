#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data.js');
const tmp = {};
for (const i in dict) {
  if (tmp[dict[i]] === undefined) {
    tmp[dict[i]] = [];
  }
  tmp[dict[i]].push(i);
}
console.log(tmp);
