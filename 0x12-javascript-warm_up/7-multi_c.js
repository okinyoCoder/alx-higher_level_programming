#!/usr/bin/node
/*
script that prints x times “C is fun”
If the first argument can’t be converted to an integer,
 it prints “Missing number of occurrences”
*/
const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
