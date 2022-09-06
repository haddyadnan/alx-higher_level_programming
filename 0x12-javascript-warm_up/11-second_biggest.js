#!/usr/bin/node
const array = process.argv.splice(2).map(Number);
if (array.length <= 3) {
  console.log(0);
} else {
  const big = Math.max(...array);
  array.splice(array.indexOf(big), 1);
  console.log(Math.max(...array));
}
