#!/usr/bin/node
const request = require('request');

const API_URL = 'https://jsonplaceholder.typicode.com/todos';

request(API_URL, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const data = JSON.parse(body);
  const users = {};
  data.forEach(task => {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  });
  console.log(users);
});
