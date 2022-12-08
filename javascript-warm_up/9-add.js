#!/usr/bin/node
/*
add function
*/

(function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
})();
