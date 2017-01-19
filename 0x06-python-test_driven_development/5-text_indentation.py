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
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print('\n'.join([line.strip() for line in text.split('\n')]), end="")
