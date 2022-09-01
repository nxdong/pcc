"""Main module."""

from ast import parse
import sys
from .python.vistor_impl import PythonVisitor
from .node_abc import ASTNodeType
from .vistor_abc import ASTVisitorType
from .parser_abc import ASTParserType
import typing


def get_vistor(language: str) -> ASTVisitorType:
    if language == 'python':
        return PythonVisitor()
    raise Exception("Language vistor not support: {}".format(language))


def get_parser(language: str) -> ASTParserType:
    if language == 'python':
        from .python import PythonParser
        return PythonParser()
    raise Exception("Language parser not support: {}".format(language))


def parse_code(code: str, parser: ASTParserType) -> ASTNodeType:
    return parser.parse(code)


def calc_code_complexity(code: str, lan: str):
    parser = get_parser(lan)
    node = parse_code(code, parser)
    visitor = get_vistor(lan)
    visitor.do_visit(node)
    # for graph in visitor.edge_list:
    #     print(graph.name, graph.complexity(),
    #           graph.lineno, graph.column)

    return visitor.edge_list
