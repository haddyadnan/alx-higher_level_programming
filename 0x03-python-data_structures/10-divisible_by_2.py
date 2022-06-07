#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    my_list2 = my_list.copy()
    for i, item in enumerate(my_list):
        if item % 2 == 0:
            my_list2[i] = True
        else:
            my_list2[i] = False
    return my_list2
