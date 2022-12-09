#!/usr/bin/node
/*
calcul factoriel
*/

function fact (nbr) {
  let i;
  let facto;
  let f = 1;
  for (i = 1; i <= facto; i++) {
    f = f * i;
  }
  return f;
}
console.log(fact(process.argv[2]));
