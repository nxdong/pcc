from ..parser_abc import ASTParserAbstractClass
from ..node_abc import ASTNodeType
from .node_impl import PythonNode
from tree_sitter import Language
from tree_sitter import Parser
from tree_sitter import Node
from ..utils import get_language_lib_path


class PythonParser(ASTParserAbstractClass):
    def __init__(self):
        super().__init__()
        G_SO_PATH = get_language_lib_path('python')
        G_LANG_HANDLE = Language(G_SO_PATH, 'python')
        self.parser = Parser()
        self.parser.set_language(G_LANG_HANDLE)

    def parse(self, code: bytes) -> PythonNode:
        tree = self.parser.parse(code)
        return PythonNode(tree.root_node)
