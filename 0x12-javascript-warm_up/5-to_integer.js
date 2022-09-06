#!/usr/bin/node
const c = isNaN(parseInt(process.argv[2]));
if (c === false) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
