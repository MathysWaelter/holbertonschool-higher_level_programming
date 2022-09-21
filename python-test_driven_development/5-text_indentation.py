#!/usr/bin/python3
"""Function to to check test indent"""


def text_indentation(text):
    """checker"""
    if type(text) is not str or text != text:
        raise TypeError("text must be a string")
    if text:
        text = text.replace('.', '.\n\n')
        text = text.replace('?', '?\n\n')
        text = text.replace(':', ':\n\n')
    print(text)
    