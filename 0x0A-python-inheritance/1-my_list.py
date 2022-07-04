#!/usr/bin/python3

"""
This module contains a class MyList that inherits from list
"""


class MyList(list):

    """
    Class MyList - Inherits from list
    """

    def print_sorted(self):

        """
        prints sorted list
        """

        print(sorted(self))
