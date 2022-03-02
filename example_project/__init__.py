"""Testowy_projekt"""
TEST_VAR = 1


def f1():
    return 1

from . import _version
__version__ = _version.get_versions()['version']
