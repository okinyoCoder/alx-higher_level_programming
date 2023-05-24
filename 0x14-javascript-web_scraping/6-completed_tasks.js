#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const users = JSON.parse(body);
    const newDict = {};
    for (let i = 0; i < users.length; i++) {
      const status = (users[i].completed);
      const key = users[i].userId.toString();
      if (status) {
        if (newDict[key]) {
          newDict[key]++;
        } else {
          newDict[key] = 1;
        }
      }
    }
    console.log(newDict);
  }
});
