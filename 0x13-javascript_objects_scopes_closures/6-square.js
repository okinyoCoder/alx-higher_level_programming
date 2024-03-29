#!/usr/bin/node
/*
 *class Square that defines a square and inherits from
 *Rectangle of 5-square.js
*/

const prevClass = require('./5-square');

class Square extends prevClass {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('c'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
