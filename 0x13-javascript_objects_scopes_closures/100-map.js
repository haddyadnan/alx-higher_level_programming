#!/usr/bin/node
const list = require('./100-data.js').list;
const multiply = function (a, b) { return a * b; };
const maps1 = list.map((x, i) => multiply(x, i));
console.log(list);
console.log(maps1);
