#!/usr/bin/python3

"""
This module prints a text with 2 new lines \
after each of these characters: .,? and :
"""


def text_indentation(text: str):

    """
    Print 2 line after occurence of [.,:,?]
    Return:
        (string) text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    hold = ""
    for txt in text:
        if txt in [".", "?", ":"]:
            hold += f"{txt}\n"
        else:
            hold += hold.join(txt)
    # print(hold.strip("\n"))
    # hold = hold.strip("\n")
    for h in hold:
        print(h, end="")
