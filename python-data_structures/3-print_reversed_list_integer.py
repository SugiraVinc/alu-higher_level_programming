#!/usr/bin/python3
# A function that reverses elements
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
print_reversed_list_integer()
