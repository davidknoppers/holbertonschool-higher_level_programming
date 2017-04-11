#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import requests

r = requests.get('https://intranet.hbtn.io/status')
print(r.headers['X-Request-Id'])