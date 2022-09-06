#!/usr/bin/node
const fact = parseInt(process.argv[2]);
function factorial (x) {
  if (x === 1 | x === 0 | (isNaN(x) === true)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

console.log(factorial(fact));
