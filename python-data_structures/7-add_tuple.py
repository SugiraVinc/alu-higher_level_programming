#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tuple_c = []
    add_a = []
    add_b = []
    if len_a >= 2 and len_b >= 2:
        tuple_c.append(tuple_a[0] + tuple_b[0])
        tuple_c.append(tuple_a[1] + tuple_b[1])
        add_b = tuple(tuple_c)
        return add_b
    if len_a < 2 and len_b < 2:
        if len_a < 1:
            add_a = list(tuple_a)
            add_a.append(0)
            add_b.append(0)
        if len_b < 1:
            add_b = list(tuple_b)
            add_b.append(0)
            add_b.append(0)
        if len_a == 1:
            add_a = list(tuple_a)
            add_a.append(0)
        if len_b == 1:
            add_b = list(tuple_b)
            add_b.append(0)
        if len_a >= 2:
            add_a = list(tuple_a)
        if len_b >= 2:
            add_b = list(tuple_b)
        tuple_c.append(add_a[0] + add_b[0])
        tuple_c.append(add_a[1] + add_b[1])
        add_b = tuple(tuple_c)
        return add_b
