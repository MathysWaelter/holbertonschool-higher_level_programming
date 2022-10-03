#!/usr/bin/python3
"""main file for my project"""


class Base:
    """main class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
