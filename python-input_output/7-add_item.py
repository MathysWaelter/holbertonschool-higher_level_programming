#!/usr/bin/python3
"""function to save JSON file"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    jsonfile = load_from_json_file("add_item.json")
except FileNotFoundError:
    jsonfile = []

for i in range(1, len(sys.argv)):
    jsonfile.append(sys.argv[i])
save_to_json_file(jsonfile, "add_item.json")
