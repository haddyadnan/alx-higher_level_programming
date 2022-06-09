#!/usr/bin/python3


def weight_average(my_list=[]):

    if (my_list is None) or (my_list == []):
        return 0
    num = 0
    denum = 0
    for i, j in my_list:
        num += i * j
        denum += j
    return num / denum
