#!/usr/bin/node
/*
A script that prints a square
The first argument is the size of the square
If the first argument can’t be converted to an integer,
  print “Missing size”
*/
const x = parseInt(process.argv[2]);
const ch = 'X';

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 1; i < x; i++) {
    for (let j = 1; j < i; j++) {
      console.log(ch);
    }
  }
}
