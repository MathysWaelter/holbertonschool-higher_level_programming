#!/usr/bin/python3
"""Function to to check test indent"""


def text_indentation(text):
    """checker"""
    if type(text) is not str or text != text:
        raise TypeError("text must be a string")

    newstr = text.replace('.', '.\n\n')
    newstr = newstr.replace('?', '?\n\n')
    newstr = newstr.replace(':', ':\n\n')
    backline = newstr.split("\n")
    for i in range(len(backline)):
        print("{}".format(backline[i].strip()),
            end=("" if (i == (len(backline) -1)) else '\n'))
