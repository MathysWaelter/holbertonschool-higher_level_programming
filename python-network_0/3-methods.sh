#!/bin/bash
#  Bash script that takes in a URL and displays all HTTP methods the server will accept.
echo $(curl -i -s -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2- | tr -d '\r\n')
