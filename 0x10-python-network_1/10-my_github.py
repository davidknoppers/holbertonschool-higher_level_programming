#!/usr/bin/python3
"""
basic interaction with github API
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        url = 'https://api.github.com/users/' + username
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print(r.json()['id'])
    except:
        print("None")
