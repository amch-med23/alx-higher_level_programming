#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Change == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Change != operator with == behavior"""
        return self.real == value
