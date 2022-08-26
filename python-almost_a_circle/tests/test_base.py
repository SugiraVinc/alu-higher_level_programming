#!/usr/bin/python3
"""Unittest for base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittest instant"""

    def test_None_id(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)
