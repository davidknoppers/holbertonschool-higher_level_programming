#!/usr/bin/node

if (isNaN(process.argv.slice(2)[0])) {
  console.log('Missing size');
} else {
  var x = 'X';
  const size = parseInt(process.argv.slice(2)[0]);
  for (var i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
}
