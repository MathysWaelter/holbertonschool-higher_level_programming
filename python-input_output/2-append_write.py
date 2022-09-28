#!/usr/bin/python3
"""function to open and append in file"""


def append_file(filename="", text=""):
    """open and append"""

    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
