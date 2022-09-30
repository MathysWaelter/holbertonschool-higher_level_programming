#!/usr/bin/python3
"""function to save JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to text file"""

    with open(filename, mode='w', encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(my_obj))
