#!/usr/bin/node
/*
 *class Rectangle that defines a rectangle
 *constructor must take 2 arguments w and h
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.h; i++) {
      for (let j = 0; j < this.j; j++) {
        console.log('X');
      }
    }
  }
}
module.exports = Rectangle;
