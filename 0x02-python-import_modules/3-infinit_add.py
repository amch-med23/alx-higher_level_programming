#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv) - 1
    if args_len == 0:
        print(args_len)
    else:
        i = 1
        temp = 0
        while i <= args_len:
            val = int(sys.argv[i])
            temp = val + temp
            i += 1
        print(temp)
