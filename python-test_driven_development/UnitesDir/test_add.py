#!/usr/bin/python3
import unittest
from 0-add_integer import add_integer
class testAdd(unittest.TestCase):

    def test_add_integer(self):
        result = add_integer.add_integer('b', 5)
        self.assertEqual(result)
