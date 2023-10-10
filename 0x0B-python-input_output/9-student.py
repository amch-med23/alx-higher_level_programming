#!/usr/bin/python3
""" this module defines a class Student """


class Student:
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        """ initializes a new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ gets the dictionary representation of the Student """
        return self.__dict__
