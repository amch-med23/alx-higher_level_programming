#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv) - 1
    if (args_len == 0):
        print("{} arguments.".format(args_len))
    else:
        i = 1
        print("{} arguments:".format(args_len))
        while i <= args_len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
