#!/usr/bin/python3
"""main file for my project"""


class Base:
    """main class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
            type(Base).id += 1
        else:
            type(Base).__nb_objects += 1
