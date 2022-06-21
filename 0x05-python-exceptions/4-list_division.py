#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    cont = []
    i = 0
    if list_length <= 0:
        print("out of range")
        return cont
    while i < list_length:
        try:
            cont.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            cont.append(0)
        except TypeError:
            print("wrong type")
            cont.append(0)
        except IndexError:
            print("out of range")
            cont.append(0)
        finally:
            i += 1
    return cont
