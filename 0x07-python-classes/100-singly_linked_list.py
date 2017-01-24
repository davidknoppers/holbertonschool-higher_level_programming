#!/usr/bin/python3
"""
Implementation of a basic singly linked list in Python
Sorted lowest to highest by node value
Offers basic print function
"""


class Node(object):
    """
    creates node with next set to None as default
    """
    def __init__(self, data, next_node=None):
        if type(data) is not int or isinstance(data, bool):
            raise TypeError('data must be an integer')
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        getter for data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        setter for data
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        getter for node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for node
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next must be a Node object')
        self.__next_node = value


class SinglyLinkedList(object):
    """
    Singly linked list
    Uses node class
    Contains a print function and sorts by int value
    """
    def __init__(self):
        """
        init
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts by int value
        """
        if not self.__head:
            self.__head = Node(value, None)
        else:
            current = self.__head
            prev = None
            while current and value > current.data:
                prev = current
                current = current.next_node
            if not current:
                prev.next_node = Node(value)
            elif current == self.__head:
                self.__head = Node(value, current)
            else:
                prev.next_node = Node(value, current)

    def __str__(self):
        """
        formats list for output
        """
        result = ""
        temp = self.__head
        while temp:
            result += str(temp.data)
            temp = temp.next_node
            if temp:
                result += '\n'
        return result
