#!/usr/bin/node
/*
check if have argv
*/

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
