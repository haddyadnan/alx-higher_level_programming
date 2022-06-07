#!/usr/bin/python3


def multiple_returns(sentence):
    sen_len = len(sentence)
    sen_first = sentence[0] if sen_len > 0 else "None"
    return sen_len, sen_first
