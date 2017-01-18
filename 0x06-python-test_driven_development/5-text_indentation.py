#!/usr/bin/python3
"""
text_indentation - inserts newlines after .:?
Requires a string input, otherwise raises errors
Prints the result
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = ""
    seps = ".?:"
    flag = 0
    for char in text:
        if char in seps:
            result += '\n\n'
            flag = 1
        elif flag == 1:
            flag = 0
            continue
        else:
            result +=char
    print(result)
