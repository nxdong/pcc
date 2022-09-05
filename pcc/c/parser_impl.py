from ..parser_abc import ASTParserAbstractClass
from ..node_abc import ASTNodeType
from .node_impl import CNode
from tree_sitter import Language
from tree_sitter import Parser
from tree_sitter import Node
from ..utils import get_language_lib_path



class CParser(ASTParserAbstractClass):
    def __init__(self):
        super().__init__()
        G_SO_PATH = get_language_lib_path('c')
        G_LANG_HANDLE = Language(G_SO_PATH, 'c')
        self.parser = Parser()
        self.parser.set_language(G_LANG_HANDLE)

    def parse(self, code: bytes) -> CNode:
        tree = self.parser.parse(code)
        return CNode(tree.root_node)
