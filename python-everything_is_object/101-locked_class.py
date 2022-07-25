#!/usr/bin/python3
'''
A BLOCKED CLASS THAT PREVENTS DYNAMIC CREATION OF INSTANCES
'''


class LockedClass(object):
    '''
    WE USE SLOT
    '''
    __slots__ = 'first_name'
