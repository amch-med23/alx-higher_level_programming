#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for x in range(0, list_lenght):
        try:
            op = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            op = 0
        except ZeroDivisionError:
            print("division by 0")
            op = 0
        except IndexError:
            print("out of range")
            op = 0
        finally:
            n_list.append(op)
    return (n_list)
