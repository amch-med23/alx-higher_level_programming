#!/usr/bin/python3


def add_integer(a, b=98):
    """this Return the sum of two integers or floats as integers
    Args:
        a: the first argument
        b: the second argument
    Returns:
           this sum of the two arguments
    Raises:
          TypeError: if either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
