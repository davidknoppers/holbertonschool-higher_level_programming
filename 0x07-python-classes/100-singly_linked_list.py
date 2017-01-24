#!/usr/bin/python3
class Node(object):
    def __init__(self, data, next_node=None):
        self.__data = data
        if not isinstance(self.__data, int):
            raise TypeError('data must be an integer')
        self.__next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None and not isinstance(value, Node):
            raise TypeError('next must be a Node object')
        self.__next_node = value

class SinglyLinkedList(object):
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value, None)
            return
        else:
            current = self.__head
            prev = None
            while current and current.__data > current.__next_node.__data:
                prev = current
                current = current.__next_node
            if current:
                new = Node(value, current.__next)
                prev.__next_node = new
            else:
                prev.__next_node = Node(value)
    def __repr__(self):
        result = ""
        start = self.__head
        while start:
            result = result + str(start.__data) + '\n'
            start = start.__next_node
        return result
