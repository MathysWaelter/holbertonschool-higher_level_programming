#!/usr/bin/python3
"""
    func for inherits another class
"""


class Mylist(list):
    """
    list of int
    """

    def print_sorted(self):
        """
        for sort
        """

        return (sorted(self))
