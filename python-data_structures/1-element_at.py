#!/usr/bin/python3
# A function that retrieves elements from a list like in C
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    elif idx >= len(my_list):
        return "None"
    else:
        return my_list[idx]
