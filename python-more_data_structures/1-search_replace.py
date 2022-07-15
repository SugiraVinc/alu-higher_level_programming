#!/usr/bin/python3


# A function that replaces all occurences of an element
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(0, len(new_list)):
        if search == new_list[i]:
            new_list[i] = replace
    return new_list
