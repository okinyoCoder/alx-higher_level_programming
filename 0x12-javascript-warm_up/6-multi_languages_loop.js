#!/usr/bin/node
/*
script that prints 3 lines: (like 1-multi_languages.js)
but by using an array of string and a loop
*/
const myArr = ['C is fun', 'Python is cool', 'Javascript is amazing'];

for (const item in myArr) {
  console.log(myArr[item]);
}
