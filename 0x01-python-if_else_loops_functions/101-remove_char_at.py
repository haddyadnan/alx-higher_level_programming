#!/usr/bin/python3


def remove_char_at(word, n):
    if n >= 0:
        word = word[:n] + word[n + 1:]
    return word
