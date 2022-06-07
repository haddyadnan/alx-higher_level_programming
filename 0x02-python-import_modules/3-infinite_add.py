#!/usr/bin/python3


def add_args(argv):

    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(0))
    else:
        i = 1
        args_sum = 0
        while i <= n:
            args_sum += int(argv[i])
            i += 1
        print(args_sum)


if __name__ == "__main__":
    import sys

    add_args(sys.argv)
