#!/usr/bin/node

const list = process.argv.slice(2);
if (list.length === 0 || list.length === 1) {
  console.log('0');
} else {
  console.log(list.sort().reverse()[1]);
}
