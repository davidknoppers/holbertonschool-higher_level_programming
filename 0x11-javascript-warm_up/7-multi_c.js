#!/usr/bin/node

if (isNaN(process.argv.slice(2)[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv.slice(2)[0]); i++) {
    console.log('C is fun');
  }
}
