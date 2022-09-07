#!/usr/bin/node
exports.esrever = function (list) {
  const tempArray = [];
  for (let i = 0; i < list.length + 1; i++) {
    tempArray[i] = list[list.length - i];
  }
  return tempArray.splice(1);
};
