#!/usr/bin/python3
if __name__ == "__main__":
    import add from "calculator_1"
    import sub from "calculator_1"
    import div from "calculator_1"
    import mul from "calculator_1"
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))