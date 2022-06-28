#!/usr/bin/python3
import dis 

def magic_calculation(a, b):
    b=98
    a=a**b
    return a+b

dis.dis(magic_calculation)
