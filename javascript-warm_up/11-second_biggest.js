#!/usr/bin/node
/*
search second biggest nbr in argv
*/

if (process.argv === undefined || process.argv[1] === undefined) {
  console.log('0');
} else {
  const arg = process.argv.slice(2);
  arg.sort((a, b) => b - a);
  console.log((arg[1]));
}
