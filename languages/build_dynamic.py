from tree_sitter import Language
import platform


def detect_platform():
    return '{}-{}'.format(platform.system(), platform.machine())


result = Language.build_library(
    # Store the library in the `languages/lib` directory
    'languages/lib/{}/{}'.format(detect_platform(), 'libpcc_ts_all.so'),

    # Include one or more languages
    [
        'languages/tree-sitter-python',
        'languages/tree-sitter-c'
    ]
)

print("Build Dynamic Lib:", result)
