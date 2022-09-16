#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value or value == 0:
            print("{:d}".format(value), end = '\n')
            return True
        else:
            return False
    except (TypeError, ValueError):
            return False
