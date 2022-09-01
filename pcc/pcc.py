"""Main module."""

from ast import parse
import sys
from .graph_vistor_impl import PathGraphingAstVisitor
from .node_abc import ASTNodeType
from .vistor_abc import ASTVisitorType
from .parser_abc import ASTParserType
import typing


def get_vistor(language: str) -> ASTVisitorType:
    if language == 'python':
        return PathGraphingAstVisitor()
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
    visitor.dispatch(node)
    for graph in visitor.graphs.values():
        print(graph.entity, graph.complexity(),
              graph.lineno, graph.column)

    return visitor.graphs
