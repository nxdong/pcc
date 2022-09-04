from multiprocessing import reduction
import os
# from charset_normalizer import from_bytes, from_path
from .config import PCC_LIB_PATH, PCC_LIB_NAME
from .config import FILE_EXT_MAP
import typing


def get_language_lib_path(_lang_name: str) -> str:
    lang_lib_path = os.path.join(PCC_LIB_PATH, PCC_LIB_NAME)
    return lang_lib_path


def uniform_charset(code_bytes: bytes) -> bytes:
    # TODO is too slow! repleace it someday
    # return from_bytes(code_bytes).best().output(encoding='utf_8')
    return code_bytes


def uniform_charset_from_file(filename) -> bytes:
    # TODO is too slow! repleace it someday
    # return from_path(filename).best().output(encoding='utf_8')
    with open(filename, 'rb') as f:
        data = f.read()
    return data


def detect_file_lanuage(filepath):
    _, ext = os.path.splitext(filepath)
    return FILE_EXT_MAP.get(ext, "NoSupport")


def travel_dir_and_filter(dir_path, exclude_dirs: typing.List[str], support_ext: typing.Mapping[str, str]) -> typing.List[str]:
    '''return supported file list'''
    ret = []

    if exclude_dirs is None:
        exclude_dirs = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # filter exclude_dir
            if dirpath.startswith(exclude_dirs):
                continue
            # filter supported file
            _, ext = os.path.splitext(filename)
            if ext in support_ext:
                ret.append(os.path.join(dirpath, filename))
    return ret
