from ..parser_abc import ASTParserAbstractClass
from ..node_abc import ASTNodeType
from .node_impl import PythonNode
from tree_sitter import Language
from tree_sitter import Parser
from tree_sitter import Node
from ..utils import get_language_lib_path

PYTHON_NAME = 'python'


def _print_node(node: Node):
    print("=========Node Info===========")
    print("Node:", node, " Type: ", type(node))
    print("dir: ", dir(node))
    print("child_by_field_id:", node.child_by_field_id)
    print("child_by_field_name:", node.child_by_field_name)
    print("child_count:", node.child_count)
    print("children:", node.children)
    print("end_byte:", node.end_byte)
    print("end_point:", node.end_point)
    print("has_changes:", node.has_changes)
    print("has_error:", node.has_error)
    print("is_missin:", node.is_missing)
    print("is_named:", node.is_named)
    print("named_child_count:", node.named_child_count)
    print("next_named_sibling:", node.next_named_sibling)
    print("next_sibling:", node.next_sibling)
    print("parent:", node.parent)
    print("prev_named_sibling:", node.prev_named_sibling)
    print("prev_sibling:", node.prev_sibling)
    print("sexp:", node.sexp)
    print("start_byte:", node.start_byte)
    print("start_point:", node.start_point)
    print("text:", node.text)
    print("type:", node.type)
    print("walk:", node.walk)
    print("=========   END   ===========")


class PythonParser(ASTParserAbstractClass):
    def __init__(self):
        super().__init__()
        so_path = get_language_lib_path(PYTHON_NAME)
        self.lang_handle = Language(so_path, PYTHON_NAME)
        self.parser = Parser()
        self.parser.set_language(self.lang_handle)

    def parse(self, code: bytes) -> PythonNode:
        # print("parser:", self.parser, " method:", dir(self.parser))
        tree = self.parser.parse(code)
        # print("tree Node:", tree, " Type: ", type(tree))
        # print("tree Node:", tree, " dir: ", dir(tree))
        # print("tree Node:", tree, " text: ", tree.text)
        # print("tree Node:", tree, " root_node: ", tree.root_node)
        root_node = tree.root_node
        _print_node(root_node)
        return PythonNode(root_node)
