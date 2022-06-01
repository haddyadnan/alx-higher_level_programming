#!/usr/bin/python3


def uppercase(c):
    word = ""

    for c in c:
        if (c != " ") & (type(c) == str):
            if ord(c) > 91:
                word += word.join(chr(ord(c) - 32))
            else:
                word += word.join(c)
        else:
            word += word.join(c)

    print("{}".format(word))
