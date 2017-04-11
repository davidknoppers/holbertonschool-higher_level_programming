#!/bin/bash
# takes in a URL as a variable, sends a request to that URL,
# sends a delete request to the URL, and displays the response
curl -LsX DELETE "$1"
