#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    t = 0
    dts = {'M': 1000,'D': 500, 'C' : 100, 'X': 10, 'L': 50, 'I': 1, 'V': 5}
    for rom in reversed(roman_string):
        ar = dts[rom]
        t += ar if t < ar * 5 else -ar
    return (t)
