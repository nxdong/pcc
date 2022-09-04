from tree_sitter import Language
import os
import platform


def detect_platform():
    return '{}-{}'.format(platform.system(), platform.machine())


def get_lib_name():
    p = platform.system()
    if p == 'Linux':
        return 'libpcc_ts_all.so'
    elif p == 'Darwin':
        return 'libpcc_ts_all.dylib'
    elif p == 'Windows':
        return 'libpcc_ts_all.dll'
    elif p == 'Java':
        raise Exception("{} platform not support yet!", p)


PCC_BUILD_LIB_PATH = os.environ.get('PCC_BUILD_LIB_PATH', '.pcc/')
PCC_BUILD_LIB_NAME = os.environ.get('PCC_BUILD_LIB_NAME', get_lib_name())


build_lib_name = os.path.join(PCC_BUILD_LIB_PATH, PCC_BUILD_LIB_NAME)
result = Language.build_library(
    # Store the library in the `languages/lib` directory
    build_lib_name,
    # Include one or more languages
    [
        'languages/tree-sitter-python',
        'languages/tree-sitter-c'
    ]
)

print("Build Dynamic Lib:", result)
print("Lib path:", build_lib_name)
