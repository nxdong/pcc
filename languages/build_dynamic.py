from tree_sitter import Language, Parser

Language.build_library(
    # Store the library in the `languages/lib` directory
    'languages/lib/x86-64/pcc_ts_python.so',

    # Include one or more languages
    [
        'languages/tree-sitter-python'
    ]
)

Language.build_library(
    # Store the library in the `build` directory
    'languages/lib/x86-64/pcc_ts_c.so',

    # Include one or more languages
    [
        'languages/tree-sitter-c'
    ]
)


Language.build_library(
    # Store the library in the `build` directory
    'languages/lib/x86-64/pcc_ts_all.so',

    # Include one or more languages
    [
        'languages/tree-sitter-c',
        'languages/tree-sitter-python'
    ]
)
