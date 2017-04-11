#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        temp = r.headers['X-Request-Id']
        print(temp)
    except:
        pass
