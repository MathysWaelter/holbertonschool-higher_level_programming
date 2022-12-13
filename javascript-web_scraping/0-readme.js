#!/usr/bin/node
const fs = require('fs');
const imput = process.argv;

fs.readFile(imput[2], 'utf-8', function (doesntexist, txt) {
  if (doesntexist) {
    return console.log(doesntexist);
  }
  console.log(txt);
});
