#!/usr/bin/node
const fs = require('fs');
const imput = process.argv;

fs.writeFile(imput[2], imput[3], 'utf-8', function (doesntexist, txt) {
    if (doesntexist) {
        return console.log(doesntexist)
    }
    console.log(txt);
});