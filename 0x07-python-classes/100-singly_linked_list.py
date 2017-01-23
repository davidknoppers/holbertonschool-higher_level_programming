#!/usr/bin/python3
class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        if not isinstance(self.__data, int):
            raise TypeError('data must be an integer')
        self.__next = next
    @property
    def data(self):
        return (self.__data)
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, value):
        if value != None and not isinstance(value, Node):
            raise TypeError('next must be a Node object')
        self.__next = value
class SinglyLinkedList(object):
    def __init__(self, head):
        if head != None and not isinstance(head, Node):
            raise TypeError('next must be a Node object')
        self.__head = head
    def sorted_insert(self, value):
        new = Node(value)
        current = new
        while new.data > new.__next.data:
            prev = current
            current = current.__next
    def __repr__(self):
