"""Main module."""

import sys
from .graph_vistor_impl import PathGraphingAstVisitor
from .node_abc import ASTNodeType
from .vistor_abc import ASTVisitorType
from .parser_abc import ASTParserType
import typing


def get_vistor(lan) -> ASTVisitorType:
    return PathGraphingAstVisitor()


def parse_code(code: str, parser: ASTParserType) -> ASTNodeType:
    return parser.parse(code)


def calc_node_complexity(tree_node: ASTNodeType, visitor: ASTVisitorType) -> typing.Any:
    visitor.dispatch(tree_node)
    for graph in visitor.graphs.values():
        print(graph.entity, graph.complexity(),
              graph.lineno, graph.column)

    return visitor.graphs


def calc_code_complexity(code: str, lan: str):
    node = parse_code()
    visitor = get_vistor()
    calc_node_complexity(node, visitor)
