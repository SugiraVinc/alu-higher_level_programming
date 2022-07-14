#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    line = my_list.reverse()
    if my_list is None:
        return
    else:
        for i in line:
            print("{:d}".format(i))
