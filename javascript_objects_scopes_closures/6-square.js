#!/usr/bin/node
const exSquare = require('./5-square');

class Square extends exSquare {
  charPrint (c) {
    const X = 'X';
    if (!c) {
      for (let i = 0; i < this.width; i++) {
        console.log(X.repeat(this.height));
      }
    } else {
      for (let j = 0; j < this.width; j++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
