#!/usr/bin/node

let request = require('request');
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let data = JSON.parse(body);
  let dict = {};
  for (let item = 0; item < data.length; item++) {
    let id = data[item]['userId'];
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
