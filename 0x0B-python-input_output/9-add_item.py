#!/usr/bin/python3
import sys
"""
module contains one function
the function takes args from sys.argv and adds them to a json file
that file is called add_item.json
"""
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

if __name__ == "__main__":

    try:
        contents = load_from_json_file('add_item.json')
    except:
        contents = []
    save_to_json_file(contents + sys.argv[1:], 'add_item.json')
