#!/usr/bin/python3
# A function that retrieves elements from a list like in C 
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    if idx >= len(my_list):
        return "None"
