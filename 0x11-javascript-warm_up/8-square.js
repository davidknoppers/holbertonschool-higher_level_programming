#!/usr/bin/node

if (isNaN(process.argv.slice(2)[0])) {
  console.log('Missing size');
} else {
  const x = 'X';
  const size = parseInt(process.argv.slice(2)[0]);
  for (let i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
}
