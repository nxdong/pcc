from ..node_abc import ASTNodeAbstractClass
from ..node_abc import ASTNodeType
from tree_sitter import Node
import typing


class PythonNode(ASTNodeAbstractClass):
    LineNo = typing.TypeVar('LineNo', int)
    ColumnNo = typing.TypeVar('ColumnNo', int)

    def __init__(self, node: Node) -> None:
        self.node = node

    @property.getter
    def type(self) -> str:
        '''return python node type'''
        return self.node.type

    @property.getter
    def child_count(self) -> int:
        '''childs count'''
        return self.node.child_count

    @property.getter
    def start_point(self) -> typing.Tuple[LineNo, ColumnNo]:
        '''start point: (LineNo, ColumnNo)'''
        return self.node.start_point

    @property.getter
    def end_point(self) -> typing.Tuple[LineNo, ColumnNo]:
        '''end point: (LineNo, ColumnNo)'''
        return self.node.end_point

    @property.getter
    def start_byte_index(self) -> int:
        '''node code start index'''
        return self.node.start_byte

    @property.getter
    def end_byte_index(self) -> int:
        '''node code end index'''
        return self.node.end_byte

