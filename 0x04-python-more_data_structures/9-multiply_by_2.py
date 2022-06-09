#!/usr/bin/python3


def multiply_by_2(my_dict):
    my_dict2 = my_dict.copy()
    for key in my_dict2.keys():
        my_dict2[key] *= 2
    return my_dict2
