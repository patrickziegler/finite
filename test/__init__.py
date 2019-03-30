import os
import unittest


def find_all():
    return unittest.defaultTestLoader.discover(os.path.dirname(__file__))
