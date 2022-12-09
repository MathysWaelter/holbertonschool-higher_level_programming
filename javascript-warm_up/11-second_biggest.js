#!/usr/bin/node
/*
search second biggest nbr in argv
*/

function SecondBiggest (arg) {
  let largest = 0; let secondLargest = 0; let i; let j;
  if (process.argv === undefined || process.argv[1] === undefined) {
    console.log('0');
  }
  for (i of arg) {
    if (i > largest) {
      largest = i;
    }
  }
  for (j of arg) {
    if (j > secondLargest && j < largest) {
      secondLargest = j;
    }
  }
  return secondLargest;
}
console.log(SecondBiggest(process.argv));
