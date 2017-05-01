#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let count = 0;
  for (const e of JSON.parse(body)['results']) {
    for (const subE of e['characters']) {
      if (subE.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
