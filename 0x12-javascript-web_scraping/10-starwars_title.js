#!/usr/bin/node

var request = require('request');

var params = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET'
};
request(params, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body)['title']);
});
