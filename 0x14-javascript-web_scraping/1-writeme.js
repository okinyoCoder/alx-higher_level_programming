#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[1];
const text = process.argv[2];


fs.writeFile('filePath', text, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});

