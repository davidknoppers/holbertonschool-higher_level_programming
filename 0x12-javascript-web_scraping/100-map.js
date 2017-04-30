#!/usr/bin/node

var list = require('./100-data').list;
console.log(list);
list.map((val, index) => {
  list[index] = val * index;
});
console.log(list);
