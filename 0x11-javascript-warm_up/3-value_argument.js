#!/usr/bin/node

process.argv.slice(2);
if (process.argv.slice(2)[0] == null) {
  console.log('No argument');
} else {
  console.log(process.argv.slice(2)[0]);
}
