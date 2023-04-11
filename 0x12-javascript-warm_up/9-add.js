#!/usr/bin/node
/*
script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
*/
const process = require('process');
function add (a, b) {
  const c = a + b;
  return c;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
