from tree_sitter import Language
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


result = Language.build_library(
    # Store the library in the `languages/lib` directory
    'languages/lib/{}/{}'.format(detect_platform(), get_lib_name()),
    # Include one or more languages
    [
        'languages/tree-sitter-python',
        'languages/tree-sitter-c'
    ]
)

print("Build Dynamic Lib:", result)
