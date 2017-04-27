#!/usr/bin/node

if (isNaN(process.argv.slice(2)[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv.slice(2)[0]);
}
