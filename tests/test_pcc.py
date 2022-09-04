#!/usr/bin/env python

"""Tests for `pcc` package."""

import pytest

from click.testing import CliRunner

from pcc import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert "Error: Missing argument 'CODE_PATH'." in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Cyclomatic Complexity Caculator' in help_result.output


def test_command_line_interface_single_py():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['tests/data/python3/ifs.py'])
    assert help_result.exit_code == 0
    assert 'Cyclomatic Complexity Caculator' in help_result.output


def test_command_line_interface_dir_py():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['tests/data/python3/'])
    assert help_result.exit_code == 0
    assert 'Cyclomatic Complexity Caculator' in help_result.output
