#!/usr/bin/node
const request = require('request');
const imput = process.argv;

request(imput[2], function (doesntexist, status) {
  if (doesntexist) throw doesntexist;
  console.log("code: ",status.statusCode);
});
