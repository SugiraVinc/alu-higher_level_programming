#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        lst_copy = my_list[:]
        return lst_copy
    elif idx >= len(my_list):
        ls_copy = my_list[:]
        return ls_copy
    else:
        second_copy = my_list[:]
        second_copy[idx] = element
        return second_copy
