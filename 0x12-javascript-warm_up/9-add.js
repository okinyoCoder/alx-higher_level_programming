#!/usr/bin/node
/*
script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
*/
const process = require('process');
function add (a, b) {
  return (a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));
