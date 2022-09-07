#!/usr/bin/node
exports.nbOccurences = function (array, searchElement) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === searchElement) {
      count++;
    }
  }
  return count;
};
