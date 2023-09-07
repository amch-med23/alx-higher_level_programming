#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, div, sub
    args_len = (len(sys.argv) - 1)
    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    ops = {'+': add, '-': sub, '/': div, '*': mul}
    if op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[op](a, b)))
