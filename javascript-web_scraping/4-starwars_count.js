#!/usr/bin/node
const request = require('request');
const imput = process.argv;

request(imput[2], function (doesntexist, status, txt) {
  if (doesntexist) {
    console.log(doesntexist);
  } else {
    let counter = 0;
    const movie = (JSON.parse(txt).results);
    for (let i = 0; i < movie.length; i++) {
      for (let y = 0; y < movie[i].characters.length; y++) {
        if (movie[i].characters[y].includes('18')) {
          counter = counter + 1;
        }
      }
    }
    console.log(counter);
  }
});
