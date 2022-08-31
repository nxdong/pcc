from abc import ABC
from abc import abstractmethod
import typing
from collections.abc import Iterator
from typing_extensions import Self
from .node_abc import ASTNodeType
ASTParserType = typing.TypeVar('ASTParserType', bound='ASTParserAbstractClass')


class ASTParserAbstractClass(ABC):
    """Performs a depth-first walk of the AST."""

    def __init__(self):
        self.language_name = "None"
        self.ext_name = []

    @abstractmethod
    def parse(self, code) -> ASTNodeType:
        '''return '''
        pass
