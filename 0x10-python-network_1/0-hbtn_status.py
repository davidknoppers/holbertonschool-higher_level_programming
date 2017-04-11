#!/usr/bin/python3
"""
Simple Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        content_type = type(content)
        utf_content = content.decode('utf-8')
        print("Body response:\n\t- type: {}".format(content_type))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf_content))
