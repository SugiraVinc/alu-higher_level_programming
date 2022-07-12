#!/usr/bin/python3
def no_c(my_string):
    x = ""
    for i in my_string:
        if (i.lower()) == 'c':
            continue
        x += i
    return x
