#!/usr/bin/python3
"""function to open and write in file"""


def write_file(filename="", text=""):
    """open and write"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
