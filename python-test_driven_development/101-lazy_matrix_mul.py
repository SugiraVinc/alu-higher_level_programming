#!/usr/bin/python3
"""A module to use Numpy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Executional function for multiplication"""
    res = np.dot(m_a,m_b)
    return(res)
    
