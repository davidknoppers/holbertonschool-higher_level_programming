#!/bin/bash
# takes in a URL as a variable, sends a request to that URL,
# and displays only the body of a 200 status code response
curl -Lsf -X GET "$1"
