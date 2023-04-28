#!/bin/bash
# takes in a URL and displays the size of the body of the response
curl -sI "$1" | grep -iF 'Content-Length' | cut -d ' '  -f 2
