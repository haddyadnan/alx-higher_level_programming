#!/usr/bin/python3


def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    best_score = max(my_dict.values())
    for key, value in my_dict.items():
        if value is best_score:
            return key
