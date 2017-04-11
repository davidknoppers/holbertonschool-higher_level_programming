#!/bin/bash
# Takes in a URL as an arg, sends a GET request to the URL, and displays the body of the response
curl -X GET -s -H "X-Holbertonschool-User-Id: 98" $1
