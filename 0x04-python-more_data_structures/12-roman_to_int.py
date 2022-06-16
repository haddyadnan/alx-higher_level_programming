#!/usr/bin/python3


def roman_to_int(roman_string):

    """
    ROUGH TRIAL:
    -   TO BE OPTIMIZED
    """
    if type(roman_string) == str:

        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_list = list(roman_string)
        n = len(roman_list)
        if n < 1:
            return roman_list
        else:
            total = 0
            for i in range(n + 1):
                if i == (n - 1):
                    total += roman_dict[roman_list[i]]
                    break
                elif roman_dict[roman_list[i]] >= roman_dict[roman_list[i + 1]]:
                    total += roman_dict[roman_list[i]]
                else:
                    total -= roman_dict[roman_list[i]]
            return total
    else:
        return 0
