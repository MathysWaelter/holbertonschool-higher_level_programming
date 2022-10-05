#!/usr/bin/python3
"""main file for my project"""


import json


class Base:
    """main class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(dict):
        """Return Json string of a dict"""
        if dict is None or len(dict) == 0:
            return "[]"
        else:
            return json.dumps(dict)
