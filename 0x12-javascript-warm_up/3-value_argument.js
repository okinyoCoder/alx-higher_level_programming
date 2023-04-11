#!/usr/bin/node
/*
script that prints a message depending
of the number of arguments passed
*/

const process = require('process');
const varArray = process.argv;
if (varArray[2] === false) {
  console.log('No argument');
} else {
  console.log(varArray[2]);
}
