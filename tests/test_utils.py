import pytest

from pcc.utils import uniform_charset, uniform_charset_from_file
from charset_normalizer import from_bytes, from_path

file_content_ground_truth = '''\
print("你好,世界")
print("hello world")
'''


def test_charset_utf8():
    file_path = './tests/data/charset/utf8.py'
    with open(file_path, 'rb') as f:
        str_bytes = f.read()
    # content = uniform_charset(str_bytes)
    # content = content.decode('utf-8')
    content = from_bytes(str_bytes).best().output(
        encoding='utf_8').decode('utf-8')
    assert content == file_content_ground_truth


def test_charset_utf8_bom():
    file_path = './tests/data/charset/utf8_bom.py'
    with open(file_path, 'rb') as f:
        str_bytes = f.read()
    # content = uniform_charset(str_bytes)
    # content = content.decode('utf-8')
    content = from_bytes(str_bytes).best().output(
        encoding='utf_8').decode('utf-8')
    assert content == file_content_ground_truth


def test_charset_file_utf8():
    file_path = './tests/data/charset/utf8.py'
    # content = uniform_charset_from_file(file_path)
    # content = content.decode('utf-8')
    content = from_path(file_path).best().output(
        encoding='utf_8').decode('utf-8')
    assert content == file_content_ground_truth


def test_charset_file_utf8_bom():
    file_path = './tests/data/charset/utf8_bom.py'
    # content = uniform_charset_from_file(file_path)
    # content = content.decode('utf-8')
    content = from_path(file_path).best().output(
        encoding='utf_8').decode('utf-8')
    assert content == file_content_ground_truth
