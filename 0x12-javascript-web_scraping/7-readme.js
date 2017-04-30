#!/usr/bin/node

var fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function read (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
