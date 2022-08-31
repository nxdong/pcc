from abc import ABC
from abc import abstractmethod
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
        pass

    @abstractmethod
    def type(self) -> typing.AnyStr:
        '''return node type'''
        pass

