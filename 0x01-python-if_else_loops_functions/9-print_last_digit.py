#!/usr/bin/python3


def print_last_digit(num):

    if num < 0:
        lastd = abs(num) % 10
        lastd = -1 * lastd
    else:
        lastd = num % 10
    print("{}".format(lastd))
    return lastd
