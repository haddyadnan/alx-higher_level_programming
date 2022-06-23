#!/usr/bin/python3

"""A single Node class
This module demonstrates creating a Singly linked list
"""


class Node:

    """
    Class Node for the singly linked list

    """

    def __init__(self, data, next_node=None):
        """
        init instance - Instantiation
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        private instance attribute - data
        property getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        private instance: attribute - data
        setter
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        private instance: attribute - next_node
        property getter
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        private instance: attribute - next node
        setter
        """
        if not ((value is None) or (type(value) == Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class: Singly linked list
    """

    def __init__(self):

        """
        Instantiating head
        """

        self.__head = None

    def __repr__(self):

        """
        repr - print output
        """

        temp = self.__head
        lsts = ""

        cont = []
        while temp:
            cont.append(temp.data)
            temp = temp.next_node

        cont.sort()
        i = 0
        while i < len(cont):

            if i < (len(cont) - 1):
                lsts += f"{cont[i]:d}"
                lsts += "\n"
            else:
                lsts += f"{cont[i]:d}"
            i += 1

        return lsts

    def sorted_insert(self, value):

        """sort elements in the linked list"""

        if self.__head is None:
            self.__head = Node(value)
        else:
            temp = self.__head
            prev = None

            while temp:

                prev = temp
                temp = temp.next_node

            if temp is None:
                prev.next_node = Node(value)

            elif (temp == self.__head) and (prev is None):
                self.__head == Node(value, temp)
            else:
                new_node = Node(value, temp)
                prev.next_node = new_node
