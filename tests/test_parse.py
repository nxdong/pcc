#!/usr/bin/env python

"""Tests for `pcc` package."""

import pytest

from click.testing import CliRunner

from pcc import pcc
from pcc import cli
import pcc

import typing


def help_travel_tree(code: str):
    pcc.parse_code(code, pcc.PythonParser())


def test_tree_sitter():
    """Tree Sitter Playground"""

    src = bytes("""def foo():
    if bar:
        baz()
""", "utf8")
#     src = bytes("""
# import sys
# """, "utf8")

    help_travel_tree(src)

