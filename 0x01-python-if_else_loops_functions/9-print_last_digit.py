#!/usr/bin/python3


def print_last_digit(num):

    if num < 0:
        lastd = abs(num) % 10
        lastd = -1 * lastd
    else:
        lastd = num % 10
    return lastd


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
