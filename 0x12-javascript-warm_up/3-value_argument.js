#!/usr/bin/node
/*
script that prints a message depending
of the number of arguments passed
*/

const firstVar = process.argv[2];
const argvLength = process.argv.length;
if (argvLength < 3) {
  console.log('No argument');
} else {
  console.log(firstVar);
}
