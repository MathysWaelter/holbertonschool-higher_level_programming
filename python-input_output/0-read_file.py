#!/usr/bin/python3
"""function to open and read file"""


def read_file(filename=""):
    """"open and read"""
    with open(filename, encoding='utf-8') as file:
            print(file.read(), end='')
