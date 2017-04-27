#!/usr/bin/node

function callMeMoby (x, funktion) {
  for (let i = 0; i < x; i++) {
    funktion();
  }
}

exports.callMeMoby = callMeMoby;
