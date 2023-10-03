#!/usr/bin/python3
"""
This module contains and defines a function that multiplies two matrices
"""

import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints or floats): The first given matrix.
        m_b (list of lists of ints or floats): The second given matrix.
    """
    return (npy.matmul(m_a, m_b))
