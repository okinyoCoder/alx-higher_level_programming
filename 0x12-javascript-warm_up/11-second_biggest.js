#!/usr/bin/node
/**
 *script that searches the second biggest integer in
 *the list of arguments
 *
*/
const process = require('process');
const arrayList = process.argv;

// slice array from second index and sort array
const x = arrayList.slice(2).sort();

if (x.length < 3) {
  console.log('0');
} else if (x.length === 3) {
  console.log('0');
} else {
  /* for (let i = 0; i < x.length; i++) {
    console.log(x[i]);
  }
 */
  console.log(x[x.length - 2]);
}
