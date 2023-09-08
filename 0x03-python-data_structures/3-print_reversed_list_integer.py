#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenth = len(my_list) - 1
    while lenth >= 0:
        print("{:d}".format(my_list[lenth]))
        lenth -= 1
