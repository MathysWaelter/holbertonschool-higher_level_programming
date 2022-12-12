#!/usr/bin/node
const request = require('request');
const imput = process.argv;
const sw = 'https://swapi-api.hbtn.io/api/films/' + imput[2];

request(sw, function (doesntexist, status, txt) {
  if (doesntexist) throw doesntexist;
  console.log(JSON.parse(txt).title);
});
