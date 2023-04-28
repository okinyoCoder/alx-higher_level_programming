#!/bin/bash
# script that takes in a URL and show all HTTP methods the server accepts
curl -sI "$1" | grep -iF 'allow' | cut -d ' ' -f 2-
