from abc import ABC
import typing
from collections.abc import Iterator
from typing_extensions import Self

ASTNodeType = typing.TypeVar('ASTNodeType', bound='ASTNodeAbstractClass')


class ASTNodeAbstractClass(ABC):
    """Performs a depth-first walk of the AST."""

    def __init__(self, root):
        self.root = root
        self.cur = root
        self._cache = {}

    def trave_child(self) -> Iterator:
        '''return iteratable object'''
        print("Abc trave_child")
        return [self]

    def type(self) -> typing.AnyStr:
        pass


# ============= Temp TEST ===========

class MyNode(ASTNodeAbstractClass):
    def trave_child(self) -> Iterator:
        '''return iteratable object'''
        print("MyAST trave_child")
        return [MyNode(1)]


def call(o: ASTNodeType):
    obj = o.trave_child()
    print("id o:", id(o))
    print("id obj:", id(obj))


m = MyNode(1)
call(m)
