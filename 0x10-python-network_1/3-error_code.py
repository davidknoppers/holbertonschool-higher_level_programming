#!/usr/bin/python3
"""
Displays URL body or error code
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = (response.read()).decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
