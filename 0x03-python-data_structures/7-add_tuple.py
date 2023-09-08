#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)
    if i < 2:
        if i == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if j < 2:
        if j == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    final_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return final_tuple
