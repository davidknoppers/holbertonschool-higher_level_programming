#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
   header = response.info()
   print("{}".format(header['X-Request-Id']))
