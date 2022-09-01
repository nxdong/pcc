from abc import ABC
import typing
from collections.abc import Iterable
from .node_abc import ASTNodeType

ASTVisitorType = typing.TypeVar(
    'ASTVisitorType', bound='ASTVisitorAbstractClass')


class ASTVisitorAbstractClass(ABC):
    """Performs a depth-first walk of the AST."""

    def __init__(self):
        self.node = None
        self._cache = {}

    def default(self, node: ASTNodeType, *args):
        for child in node.childs():
            self.dispatch(child, *args)

    def dispatch(self, node: ASTNodeType, *args):
        print("Dispatch Node:", node)
        self.node = node
        node_type = node.type
        print("node_type:", node_type)
        meth = self._cache.get(node_type)
        if meth is None:
            meth = getattr(self.visitor, 'visit_' + node_type, self.default)
            print("Type: {}  Func: {}".format(node_type, meth))
            self._cache[node_type] = meth
        return meth(node, *args)

    def preorder(self, tree: ASTNodeType, visitor, *args):
        """Do preorder walk of tree using visitor"""
        self.visitor = visitor
        #visitor.visit = self.dispatch
        self.dispatch(tree, *args)  # XXX *args make sense?
