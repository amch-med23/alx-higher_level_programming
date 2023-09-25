#!/usr/bin/python3

def magic_calculation(a, b):
    value = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too Far')
            else:
                value += (a ** b) / x
        except Exception:
            value = b + a
            break
    return (value)
