#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        if i not in "None":

        print("{:d}".format(i))
print_reversed_list_integer()
