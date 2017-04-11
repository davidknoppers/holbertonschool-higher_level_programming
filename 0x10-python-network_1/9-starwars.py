#!/usr/bin/python3
"""
Searches the Star Wars API for names that contain the letters we pass as
sys.argv[1]
"""
import requests
import sys


search_letters = sys.argv[1]
url = "https://swapi.co/api/people/?search=" + search_letters
r = requests.get(url)
if r == {}:
    print("No result")
else:
    result_dict = dict(r.json())['results']
    for item in result_dict:
        print(dict(item)['name'])
