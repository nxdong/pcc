#!/usr/bin/env python

"""Tests for `pcc` package."""

import pytest

from click.testing import CliRunner

from pcc import pcc
from pcc import cli


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'pcc.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output


# def test_tree_sitter():
#     """Tree Sitter Playground"""
#     print("???????")
#     import tree_sitter as ts
#     print("Tree Sitter loaded! ", ts, flush=True)
#     PY_LANGUAGE = ts.Language(
#         'languages/lib/x86-64/pcc_ts_python.so', 'python')
#     parser = ts.Parser()
#     parser.set_language(PY_LANGUAGE)

#     src = bytes("""
# def foo():
#     if bar:
#         baz()
# """, "utf8")
#     src = bytes("""
# import sys
# """, "utf8")
#     tree = parser.parse(src)
#     print("Tree : ", tree)
#     cursor = tree.walk()
#     print("Root type:", tree.root_node.type)
#     print("cursor type:", cursor.node.type)

#     cursor.goto_first_child()
#     print("cursor.node.type:", cursor.node.type)

#     # Root type must be module
