#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const ID = '18';
    const data = JSON.parse(body);
    const len = data;
    const count = 0;

    for (const movie of data.results) {
      for (const character of movie.characters) {
        console.log(character);
        if (character === ID) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
