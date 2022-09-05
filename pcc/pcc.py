"""Main module."""

from ast import parse
import sys
from .node_abc import ASTNodeType
from .vistor_abc import ASTVisitorType
from .parser_abc import ASTParserType
import typing
import os
from .utils import uniform_charset_from_file
from .config import FILE_EXT_MAP


def detect_file_lanuage(filepath):
    _, ext = os.path.splitext(filepath)
    return FILE_EXT_MAP[ext]


def get_vistor(language: str) -> ASTVisitorType:
    if language == 'python':
        from .python import PythonVisitor
        return PythonVisitor()
    elif language == 'c':
        from .c import CVisitor
        return CVisitor()
    raise Exception("Language vistor not support: {}".format(language))


def get_parser(language: str) -> ASTParserType:
    if language == 'python':
        from .python import PythonParser
        return PythonParser()
    if language == 'c':
        from .c import CParser
        return CParser()
    raise Exception("Language parser not support: {}".format(language))


def parse_code(code: str, parser: ASTParserType) -> ASTNodeType:
    return parser.parse(code)


def calc_code_complexity(code: bytes, lan: str, filename: str = ''):
    parser = get_parser(lan)
    node = parse_code(code, parser)
    visitor = get_vistor(lan)
    visitor.set_filename(filename)
    visitor.do_visit(node)
    # for graph in visitor.edge_list:
    #     print(graph.name, graph.complexity(),
    #           graph.lineno, graph.column)

    return visitor.edge_list


def calc_code_complexity_from_file(filepath: str) -> list:
    language = detect_file_lanuage(filepath)
    code_bytes = uniform_charset_from_file(filepath)
    edge_list = calc_code_complexity(code_bytes, language, filepath)
    return edge_list
