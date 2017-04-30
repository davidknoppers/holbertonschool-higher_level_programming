#!/usr/bin/node

var request = require('request');
var url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  var data = JSON.parse(body);
  var dict = {};
  for (var item = 0; item < data.length; item++) {
    var id = data[item]['userId'];
    if (data[item]['completed'] === true) {
      if (dict[id] === undefined) {
        dict[id] = 1;
      } else {
        dict[id] += 1;
      }
    }
  }
  console.log(dict);
});
