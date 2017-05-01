#!/usr/bin/node

const Square = require('./5-square').Square;

Square.prototype.charPrint = function (c) {
  let array = [];
  if (c === undefined) {
    array = Array(this.width).fill(Array(this.height + 1).join('X'));
  } else {
    array = Array(this.width).fill(Array(this.height + 1).join(c));
  }
  for (let s of array) {
    console.log(s);
  }
};

exports.Square = Square;
