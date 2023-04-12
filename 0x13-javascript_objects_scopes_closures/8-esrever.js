#!/usr/bin/node
/*
 *function that returns the reversed version of a list
*/

exports.esrever = function (list) {
  const original = list.sort();
  const newArr = [];
  for (let i = original.length - 1; i >= 0; i--) {
    newArr.push(original[i]);
  }
  return newArr;
};
