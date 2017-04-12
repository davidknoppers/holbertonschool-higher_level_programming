#!/usr/bin/python3
"""
Like 101 except we also display
what films each character has appeared in
"""
import requests
import sys

if __name__ == "__main__":
    search_letters = sys.argv[1]
    url = "https://swapi.co/api/people/?search=" + search_letters
    r = requests.get(url)
    if r == {}:
        print("No result")
    else:
        print("Number of result: {}".format(dict(r.json())['count']))
        next_page = dict(r.json())['next']
        while next_page is not None:
            result_dict = dict(r.json())['results']
            for item in result_dict:
                print(dict(item)['name'])
                for film in dict(item)['films']:
                    temp = requests.get(film)
                    print("\t{}".format(dict(temp.json())['title']))
            r = requests.get(next_page)
            next_page = dict(r.json())['next']
        result_dict = dict(r.json())['results']
        for item in result_dict:
            print(dict(item)['name'])
            for film in dict(item)['films']:
                temp = requests.get(film)
                print("\t{}".format(dict(temp.json())['title']))
