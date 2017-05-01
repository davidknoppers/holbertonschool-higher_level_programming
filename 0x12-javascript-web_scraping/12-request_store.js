#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
let data = '';

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
