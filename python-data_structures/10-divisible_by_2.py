#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    num_list = list()
    for num in my_list:
        if num % 2 == 0:
            num_list.append(True)
        else:
            num_list.append(False)
    return num_list
