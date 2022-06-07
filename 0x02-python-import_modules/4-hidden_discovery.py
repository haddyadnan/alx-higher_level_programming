#!/usr/bin/python3

import hidden_4


def hidden():
    hid = dir(hidden_4)
    for i in hid:
        if i[:2] != "__":
            print("{:s}".format(i))


if __name__ == "__main__":
    hidden()
