#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename) as myFile:
        data = json.load(myFile)
        return(data)
