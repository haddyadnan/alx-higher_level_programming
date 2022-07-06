#!/usr/bin/python3

"""
This module writes all arguments to a python list
and save to a file
"""

import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    lsts = load_from_json_file(filename)
except FileNotFoundError:
    lsts = []
finally:
    for arg in sys.argv[1:]:
        lsts.append(str(arg))
    save_to_json_file(lsts, filename)
