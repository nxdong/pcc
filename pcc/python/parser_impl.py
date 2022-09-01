from ..parser_abc import ASTParserAbstractClass
from ..node_abc import ASTNodeType
from .node_impl import PythonNode
from tree_sitter import Language
from tree_sitter import Parser
from tree_sitter import Node
from ..utils import get_language_lib_path

PYTHON_NAME = 'python'


class PythonParser(ASTParserAbstractClass):
    def __init__(self):
        super().__init__()
        so_path = get_language_lib_path(PYTHON_NAME)
        self.lang_handle = Language(so_path, PYTHON_NAME)
        self.parser = Parser()
        self.parser.set_language(self.lang_handle)

    def parse(self, code: bytes) -> PythonNode:
        tree = self.parser.parse(code)
        return PythonNode(tree.root_node)
