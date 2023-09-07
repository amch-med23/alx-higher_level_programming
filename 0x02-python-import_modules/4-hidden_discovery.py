#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir(hidden_4)
    lenth = len(dir(hidden_4))
    i = 0
    while i < lenth:
        temp = (dir(hidden_4)[i])
        if (temp[0] != '_' and temp[1] != '_'):
            print("{}".format(temp))
        i += 1
