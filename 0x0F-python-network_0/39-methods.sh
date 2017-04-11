#!/bin/bash
# takes in a URL as a variable, requests all HTTP methods acceptable to that URL
curl -si "$1" | grep Allow: | cut -d':' -f2 | cut -b2-
