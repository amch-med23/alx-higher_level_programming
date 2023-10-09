#!/usr/bin/python3
"""
   this module inherits from the list class
"""


class Mylist(list):
    """ this class inherits from a list  """
    def prrint_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
