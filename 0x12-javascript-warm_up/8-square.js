#!/usr/bin/node
/*
A script that prints a square
The first argument is the size of the square
If the first argument can’t be converted to an integer,
  print “Missing size”
*/
const j = process.argv;
const ch = 'X';

if (isNaN(j)) {
  console.log('Missing size');
} else {
  const x = parseInt(j);
  for (let i = 1; i < x; i++) {
    for (let j = 1; j < i; j++) {
      console.log(ch);
    }
  }
}
