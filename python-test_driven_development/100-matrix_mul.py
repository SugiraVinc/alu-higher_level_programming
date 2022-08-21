#!/usr/bin/python3
"""A module to multiply matrices"""


def matrix_mul(m_a, m_b):
    """Our function matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_be must be a list")
    if not isinstance(m_a, (list,)):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, (list,)):
        raise TypeError("m_b must be a list of lists")
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for elements in m_a:
                if type(m_a[elements]) != int and type(m_a[elements]) != float:
                    raise TypeError("m_a should contain only integers or floats")
    for data in m_b:
        if type(m_b[data]) != int and type(m_b[data]) != float:
            raise TypeError("m_b should contain only integers or floats")
    raw_size = len(m_a[0])
    for raws in raw_size:
        if raw_size != len(m_a[0]):
            raise TypeError("m_a should contain only integers or floats")
    raw_sizeb = len(m_b[0])
    for rawsb in raw_sizeb:
        if raw_sizeb != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                if m_a[i][k] * m_b[k][j] != True:
                    raise TypeError("m_a and m_b can't be multiplied")
