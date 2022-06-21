#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    i = 0
    nums = 0
    while True:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                nums += 1
            else:
                print()
                return nums
        except (ValueError, TypeError):
            i += 1
