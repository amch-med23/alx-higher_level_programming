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
    @next_node.settr
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
        pall = ""
        loc = self.head
        while loc:
            pall += str(loc.data) + "\n"
            loc = loc.next_node
        return pall[:-1]
