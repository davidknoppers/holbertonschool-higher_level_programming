#!/usr/bin/python3
"""
Takes in a URL as argv1 and an email as argv2, sends a POST request to the URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        email_address = (response.read()).decode('utf-8')
        print(email_address)
