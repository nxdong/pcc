#!/usr/bin/env python

"""Tests for `pcc` package."""

import pytest

from click.testing import CliRunner

from pcc import pcc
from pcc import cli
import pcc

import typing


def help_get_complexity(code: str):
    code = bytes(code, "utf8")
    graphs = pcc.calc_code_complexity(code, 'python')
    if not graphs:
        return 0
    max_item = max(graphs, key=lambda x: x.complexity())
    return max_item.complexity()


def test_expr_as_statement():
    code = '''\
def f():
    0xF00D
'''
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_sequential():
    code = """\
def f(n):
    k = n + 4
    s = k + n
    return s
"""
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_sequential_unencapsulated():
    code = """\
k = 2 + 4
s = k + 3
"""
    complexity = help_get_complexity(code)
    assert complexity == 0


def test_if_elif_else_dead_path():
    code = """\
def f(n):
    if n > 3:
        return "bigger than three"
    elif n > 4:
        return "is never executed"
    else:
        return "smaller than or equal to three"
"""
    complexity = help_get_complexity(code)
    assert complexity == 3


def test_for_loop():
    code = """\
def f():
    for i in range(10):
        print(i)
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_for_else():
    code = """\
def f(mylist):
    for i in mylist:
        print(i)
    else:
        print(None)
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_recursive():
    code = """\
def f(n):
    if n > 4:
        return f(n - 1)
    else:
        return n
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_async_keywords():
    code = """\
async def foobar(a, b, c):
    await whatever(a, b, c)
    if await b:
        pass

    async with c:
        pass

    async for x in a:
        pass
"""
    complexity = help_get_complexity(code)
    assert complexity == 3


def test_annotated_assign():
    code = """\
def f():
    x: Any = None
"""
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_nested_functions():
    code = """\
def a():
    def b():
        def c():
            pass
        c()
    b()
"""
    complexity = help_get_complexity(code)
    # TODO: in https://github.com/PyCQA/mccabe project,
    # this complexity is 3.
    # but i think it maybe 1. because it can be test by one unit test.
    assert complexity == 1


def test_nested_functions_if():
    code = """\
def a():
    def b():
        def c():
            a = 10
            if a == 10:
                return true
            else:
                return false
            pass
        c()
    b()
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_try_else():
    code = """\
def try_test():
    try:
        print(1)
    except TypeA:
        print(2)
    except TypeB:
        print(3)
    else:
        print(4)
"""
    complexity = help_get_complexity(code)

    assert complexity == 4
