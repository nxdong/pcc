from ..node_abc import ASTNodeAbstractClass
from ..node_abc import ASTNodeType
from tree_sitter import Node
import typing
import json
from typing_extensions import Self


class PythonNode(ASTNodeAbstractClass):
    LineNo = int
    ColumnNo = int

    def __init__(self, node: Node) -> None:
        self.node = node
        
    @property
    def type(self) -> str:
        '''return python node type'''
        return self.node.type

    @property
    def child_count(self) -> int:
        '''childs count'''
        return self.node.child_count

    @property
    def children(self) -> typing.List[Self]:
        '''child nodes'''
        return list(map(PythonNode, self.node.children))

    @property
    def start_point(self) -> typing.Tuple[LineNo, ColumnNo]:
        '''start point: (LineNo, ColumnNo)'''
        return self.node.start_point

    @property
    def end_point(self) -> typing.Tuple[LineNo, ColumnNo]:
        '''end point: (LineNo, ColumnNo)'''
        return self.node.end_point

    @property
    def start_byte_index(self) -> int:
        '''node code start index'''
        return self.node.start_byte

    @property
    def end_byte_index(self) -> int:
        '''node code end index'''
        return self.node.end_byte

    @property
    def name(self) -> str:
        if self.node.is_named:
            name = self.node.child_by_field_name('name')
            if name and name.type == 'identifier':
                return str(name.text, encoding='utf8')
        return ''

    def __str__(self) -> str:
        return json.dumps({
            'class': self.__class__.__name__,
            'type': self.type,
            'start_point': self.start_point,
            'end_point': self.end_point,
            'child_count': self.child_count,
            'name': self.name
        })

    def __repr__(self) -> str:
        return self.__str__()
