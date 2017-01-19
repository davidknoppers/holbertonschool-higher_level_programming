#!/usr/bin/python3
"""
text_indentation - inserts newline into a text
Requires a str input, otherwise raises errors
Prints the result, no return value
"""


def text_indentation(text):
    """
    Adds newlines to a string based on sep, and prints it
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError('text must be a string')
    result = ""
    sep = ".?:"
    sep_flag = 0
    for char in text:
        if char in sep:
            if result[:-1] != " ":
                result += char
            result += '\n\n'
            sep_flag = 1
        elif sep_flag == 1:
            sep_flag = 0
            continue
        else:
            result += char
    print(result)
