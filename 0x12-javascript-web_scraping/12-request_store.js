#!/usr/bin/node

var request = require('request');
var fs = require('fs');
var url = process.argv[2];
var file = process.argv[3];
var data = '';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  data = body;
  fs.writeFile(file, data, 'utf-8', function write (err, data) {
    if (err) {
      return console.log(err);
    }
  });
});
