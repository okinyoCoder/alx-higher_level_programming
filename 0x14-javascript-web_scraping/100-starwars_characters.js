#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body);

    for (character of movies.characters) {
      request.get(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
