#!/usr/bin/python3

"""calss Node"""


class Node:
    """definign the node calss"""
    def __init__(self, data, next_node=None):
        """ Initiatin of the node with instance variable"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ this gets the data attribute """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ set data attribue """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ gets the next_data attribute
            Return: the next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Setting the value of the next node """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list class"""

    def __init__(self):
        """ Initializing the singely linked lisst"""
        self.head = None

    def __str__(self):
        """ apply the printability to the list """
        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
