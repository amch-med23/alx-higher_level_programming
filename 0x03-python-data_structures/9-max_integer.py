#!/usr/bin/python3

def max_integer(my_list=[]):
    i = len(my_list)
    if i == 0:
        return None
    else:
        max_i = my_list[0]
        for x in range(i):
            if my_list[x] > max_i:
                max_i = my_list[x]
        return max_i
