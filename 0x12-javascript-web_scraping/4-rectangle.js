#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if ((w > 0) && (h > 0)) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };
  this.rotate = function () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  };
  this.double = function () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  };
};
