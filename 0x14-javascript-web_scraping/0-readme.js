#!/usr/bin/node

const filepath = process.argv[2];
const fs = require('fs');

fs.readFile(filepath, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
