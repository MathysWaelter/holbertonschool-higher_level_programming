#!/usr/bin/python3
"""Function to to check test indent"""


def text_indentation(text):
    """checker"""
    i = 0
    newchar = ":?."
    if type(text) is not str or text != text:
        raise TypeError("text must be a string")
    while i < len(text):
        print(text[i], end="")
        if text[i] in newchar:
            print("\n")
            i = i + 2
        else:
            i = i + 1
