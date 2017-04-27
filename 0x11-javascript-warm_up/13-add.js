#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return (parseInt(a) + parseInt(b));
  }
}
exports.add = add;
