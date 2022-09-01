from abc import ABC
from abc import abstractmethod
import typing
from .node_abc import ASTNodeType

ASTVisitorType = typing.TypeVar(
    'ASTVisitorType', bound='ASTVisitorAbstractClass')


class ASTVisitorAbstractClass(ABC):
    """Performs a depth-first walk of the AST."""

    def __init__(self):
        pass

    @abstractmethod
    def do_visit(self, node: ASTNodeType):
        pass
