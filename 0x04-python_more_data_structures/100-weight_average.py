#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        den = 0
        for t in my_list:
            n += (t[0] * t[1])
            den += (t[1])
        return (n/den)
    return 0
