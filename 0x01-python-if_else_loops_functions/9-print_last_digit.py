#!/usr/bin/python3
def print_last_digit(i):
    if i < 0:
        lastdigit = i % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = i % 10
        print(last_digit, end='')
    return abs(last_digit)
