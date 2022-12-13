#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const input = process.argv;

request(input[2], function (error, responses, body) {
  if (error) throw error;
  else {
    const txt = body;
    fs.writeFile(input[3], txt, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
