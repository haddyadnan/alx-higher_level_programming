#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    my_list2 = my_list.copy()
    if (idx < 0) | (idx > (len(my_list) - 1)):
        return my_list
    else:
        my_list2[idx] = element
        return my_list2
