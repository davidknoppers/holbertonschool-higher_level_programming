#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import requests
import sys


url = sys.argv[1]
if __name__ == "__main__":
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
