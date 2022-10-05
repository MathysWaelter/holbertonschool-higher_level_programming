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
    def to_json_string(list_dictionaries):
        """Return Json string of a list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json file to string"""
        file = cls.__name__ + ".json"
        dict = []

        if list_objs is not None:
            for i in list_objs:
                dict.append(i.to_dictionary())

        string_ = cls.to_json_string(dict)

        with open(file, mode='w') as f:
            f.write(string_)
