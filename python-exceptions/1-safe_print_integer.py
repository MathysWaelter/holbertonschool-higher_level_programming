#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value:
            print("{:d}".format(value), end= '\n')
            return True
    except (TypeError, ValueError):
            return False