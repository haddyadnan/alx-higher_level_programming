#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:

        r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
        r_list = list(roman_string)
        n = len(r_list)
        if n < 1:
            return r_list
        else:
            ttl = 0
            for i in range(n + 1):
                if i == (n - 1):
                    ttl += r_dict[r_list[i]]
                    break
                elif r_dict[r_list[i]] >= r_dict[r_list[i + 1]]:
                    ttl += r_dict[r_list[i]]
                else:
                    ttl -= r_dict[r_list[i]]
            return ttl
    else:
        return 0
