#!/usr/bin/python3
"""
   this module inherits from the list class
"""


class MyList(list):
    """ this class inherits from a list  """
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
