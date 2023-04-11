#!/usr/bin/node
/*
script that prints a message depending
of the number of arguments passed
*/
import { argv } from 'node:process';

const argvLength = process.argv.length;
if (argvLength < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
