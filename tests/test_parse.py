#!/usr/bin/env python

"""Tests for `pcc` package."""

import pytest

from click.testing import CliRunner

from pcc import pcc
from pcc import cli
import pcc

import typing


def help_travel_tree(code: str):
    node = pcc.parse_code(code, pcc.PythonParser())
    print("?? node:", node)
    print("?? node type:", node.type)
    print("?? node childs:", node.childs)


def help_calc_code(code: str):
    graphs = pcc.calc_code_complexity(code, 'python')
    print("graphs===> ", list(graphs.values()))
    graph_list = list(graphs.values())
    if graph_list is None:
        return 0
    max_item = max(graph_list, key=lambda x: x.complexity())
    print("max_item:", max_item)
    return max_item.complexity()


# def test_tree_sitter():
#     """Tree Sitter Playground"""

#     src = bytes("""def foo():
#     if bar:
#         baz()
# """, "utf8")
# #     src = bytes("""
# # import sys
# # """, "utf8")

#     # help_travel_tree(src)
#     r = pcc.calc_code_complexity(src, 'python')
#     print("rrrr===> ", r)


def test_simple_statment():
    code = bytes("""a = 1""", "utf8")
    complexity = help_calc_code(code)
    print("complexity:", complexity)
    assert complexity == 1


# def test_func_statment():
#     code = bytes("""\
# def fuccccc(n):
#     k = n + 4
#     s = k + n
#     return s""", "utf8")
#     complexity = help_calc_code(code)
#     print("complexity:", complexity)
#     assert complexity == 1


# def test_if_statment():
#     code = bytes("""\
# def fuccccc(n):
#     k = n + 4
#     s = k + n
#     return s""", "utf8")
#     complexity = help_calc_code(code)
#     print("complexity:", complexity)
#     assert complexity == 1
