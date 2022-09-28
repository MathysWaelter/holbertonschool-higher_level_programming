#!/usr/bin/python3
"""function to import and return JSON file"""


import json


def to_json_string(my_obj):
    """"return dump"""
    return json.dumps(my_obj)
