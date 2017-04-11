#!/usr/bin/python3
"""
Searches the given url for an id and name based on q
q is just a server-side variable set up to generate a random JSON name-id pair
"""
import requests
import sys


if __name__ == "__main__":
    try:
        letter = sys.argv[1]
    except:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={"q": letter}).json()
    if r == {}:
        print("No result")
    else:
        print("[{}] {}".format(r['id'], r['name']))
