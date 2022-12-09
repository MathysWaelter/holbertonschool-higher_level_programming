#!/usr/bin/node
/*
calcul factoriel
*/

function fact (facto) {
  let i;
  let f = 1;
  for (i = 1; i <= facto; i++) {
    f = f * i;
  }
  return f;
}
console.log(fact(process.argv[2]));
