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
        if value is not None and not isinstance(value, Node):
            raise TypeError('next must be a Node object')
        self.__next_node = value


class SinglyLinkedList(object):
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
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

    def __repr__(self):
        result = ""
        temp = self.__head
        while temp:
            result += str(temp.data)
            temp = temp.next_node
            if temp:
                result += '\n'
        return result
