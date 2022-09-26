#!/usr/bin/python3
"""
    func for inherits another class
"""


class MyList(list):
    """
    list of int
    """

    def print_sorted(self):
        """
        for sort
        """

        print(sorted(self))
