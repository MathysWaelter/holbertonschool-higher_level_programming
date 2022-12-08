#!/usr/bin/node
/*
script that prints multiple str
*/

const count = parseInt(process.argv[2]);
let i;

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
