#!/usr/bin/node
/*
script that prints multiple str
*/

multi_str = ['C is fun'];
count = parseInt(process.argv[2]);

if (!isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log(multi_str);
  }
}
