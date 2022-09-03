import imp
import os
from sys import platform
from charset_normalizer import from_bytes, from_path
from .config import PCC_LIB_PATH, PCC_LIB_NAME


def get_language_lib_path(_lang_name: str) -> str:
    lang_lib_path = os.path.join(PCC_LIB_PATH, PCC_LIB_NAME)
    return lang_lib_path


def uniform_charset(code_bytes: bytes) -> bytes:
    return from_bytes(code_bytes).best().output(encoding='utf_8')


def uniform_charset_from_file(filename) -> bytes:
    return from_path(filename).best().output(encoding='utf_8')
