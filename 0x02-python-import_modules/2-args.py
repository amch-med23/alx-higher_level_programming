#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv) - 1
    if (args_len == 0):
        print("{} arguments.".format(args_len))
    elif args_len == 1:
        print("{} argument:".format(args_len))
    else:
        print("{} arguments:".format(args_len))
    i = 1
    while i <= args_len:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
