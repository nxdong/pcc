import os
from sys import platform


def detect_platform():
    return 'linux-x86_64'


def get_language_lib_path(lang_name: str):
    project_root_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    print("BaseDir:", project_root_dir)
    platform = detect_platform()
    lang_lib_dir = os.path.join(project_root_dir, 'languages', 'lib', platform)
    # TODO: add win/mac support
    lang_lib_name = "pcc_ts_{}.so".format(lang_name)
    lang_lib_path = os.path.join(lang_lib_dir, lang_lib_name)
    print("lang_so_path:",lang_lib_path)
    return lang_lib_path
