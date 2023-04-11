#!/usr/bin/node
/*
Write a script that prints My number:
 <first argument converted in integer>
if the first argument can be converted to an integer:
if the argument can’t be converted to an integer,
 print “Not a number”
*/

const process = require('process');
const arrayVar = process.argv;
if (isNaN(arrayVar[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arrayVar[2]);
}
