#!/usr/bin/node
/*
script that prints two arguments passed to it
*/
const numb = process.argv[2];

if (!isNaN(numb)) {
  console.log('My number: %s', process.argv[2]);
} else {
  console.log('Not a number');
}
