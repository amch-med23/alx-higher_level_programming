#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = len(my_list) - 1
    idx <= i
    if idx < 0 or idx > i:
        return my_list
    del my_list[idx]
    return my_list
