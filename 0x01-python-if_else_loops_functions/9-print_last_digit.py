#!/usr/bin/python3


def print_last_digit(num):

    exe = 0
    if num < 0:
        num *= -1
    exe = 1
    lastd = num % 10
    if exe == 1:
        num *= -1
    print("{:d}".format(lastd), end="")
    return lastd
