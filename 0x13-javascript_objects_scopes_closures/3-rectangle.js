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
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        console.log('X');
      }
    }
  }
}
module.exports = Rectangle;
