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
        for child in node.trave_child():
            self.dispatch(child, *args)

    def dispatch(self, node: ASTNodeType, *args):
        self.node = node
        klass = node.__class__
        meth = self._cache.get(klass)
        if meth is None:
            className = klass.__name__
            meth = getattr(self.visitor, 'visit' + className, self.default)
            self._cache[klass] = meth
        return meth(node, *args)

    def preorder(self, tree: ASTNodeType, visitor, *args):
        """Do preorder walk of tree using visitor"""
        self.visitor = visitor
        #visitor.visit = self.dispatch
        self.dispatch(tree, *args)  # XXX *args make sense?


# ============= Temp TEST ===========
class MyAST(ASTVisitorAbstractClass):
    def trave_child(self, node) -> Iterable:
        '''return iteratable object'''
        print("MyAST trave_child")
        pass


def call(o: ASTVisitorType):
    print(o.trave_child(1))


m = MyAST()
call(m)
