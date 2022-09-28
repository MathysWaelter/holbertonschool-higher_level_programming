#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """write and return"""
    with open (my_obj, 'w', encoding='utf-8') as JsonFile:
        JsonFile.dump(my_obj, filename)
