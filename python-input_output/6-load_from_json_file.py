#!/usr/bin/python3
""" function that creates an Object from a “JSON file”:"""


import json 


def load_from_json_file(filename):
    """load function"""
    with open(filename, 'r') as filejson:
        object = json.load(filejson)
    print(object)
