import functools
import pytest


def _skip_shadow_(func):
    print("enter _skip_shadow_")
    print(func)
    return func


@_skip_shadow_
def test_function():
    print("enter test_function")
