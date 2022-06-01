#!/usr/bin/python3

i = 122
while i >= 97:
    switch = 0
    if i % 2 != 0:
        i -= 32
        switch = 1
    print("{}".format(chr(i)), end="")
    if switch == 1:
        i += 32
    i -= 1
