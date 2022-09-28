#!/usr/bin/python3
"""function to return an object JSON string"""


import json


def from_json_string(my_str):
    """import json string"""
    a = json.loads(my_str)
    return a
