from ..vistor_abc import ASTVisitorAbstractClass
from ..graph import Verticle
from ..graph import Edge


class CVisitor(ASTVisitorAbstractClass):
    """ A visitor for a parsed Abstract Syntax Tree which finds executable
        statements.
    """

    def __init__(self):
        # last processed verticle
        self.end_verticle = None
        self.edge_list = []
        self.edge = None
        self.filename = ''

    def set_filename(self, filename):
        self.filename = filename

    def add_to_path(self, verticle):
        if not self.end_verticle:
            return
        self.edge.link_verticles(self.end_verticle, verticle)
        self.end_verticle = verticle

    def visit_statement(self, node):
        node_name = node.type
        visit_func = getattr(self, node_name+'_visitor',
                             self.linear_statement_visitor)
        return visit_func(node)

    def do_visit(self, tree):
        self.visit_statement(tree)

    def function_definition_visitor(self, node, class_name=None):
        line_start = node.start_point[0] + 1
        column_no = node.start_point[1]
        fun_name = '{}:{}'.format(node.name, line_start)
        if class_name:
            fun_name = class_name + '--' + fun_name
        fun_verticle = Verticle(fun_name)
        self.edge = Edge(self.filename, fun_name, line_start, column_no)
        self.end_verticle = fun_verticle
        self.body_visitor(node)
        self.end_verticle = None
        # FIXME: self.edge may changed in block_visitor. it's bad
        if self.edge:
            self.edge_list.append(self.edge)
        self.edge = None

    def translation_unit_visitor(self, node):
        for inode in node.children:
            self.visit_statement(inode)

    children_visitor = translation_unit_visitor

    def compound_statement_vistor(self, node):
        for inode in node.children:
            self.children_visitor(inode)

    def body_visitor(self, node):
        for inode in node.children:
            if inode.type == 'compound_statement':
                self.children_visitor(inode)

    def if_statement_visitor(self, node):
        if self.edge == None:
            return
        line_start = node.start_point[0] + 1
        name = 'if:{}'.format(line_start)
        if_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = if_verticle
        else:
            self.add_to_path(if_verticle)
        self.if_block_visitor(if_verticle, node)

    def if_block_visitor(self, begin_verticle, node):
        final_verticle = Verticle('')
        possible_end = [begin_verticle]
        for inode in node.children:
            if inode.type == 'if':
                pass
            elif inode.type == 'parenthesized_expression':
                pass
            elif inode.type == 'compound_statement':
                self.if_block_visitor(begin_verticle, inode)
                possible_end.append(self.end_verticle)
            elif inode.type == 'else':
                # if the 'if' statement has 'else' statement,
                # the 'if' statement no longer need to be linked to the final verticel
                possible_end = possible_end[1:]
                pass
            elif inode.type == 'if_statement':
                self.end_verticle = begin_verticle
                self.if_statement_visitor(inode)
                possible_end.append(self.end_verticle)
            else:
                self.compound_statement_vistor(inode)

        for iend in possible_end:
            if self.edge is None:
                continue
            self.edge.link_verticles(iend, final_verticle)
        self.end_verticle = final_verticle

    def try_block_visitor(self, begin_verticle, node):
        final_verticle = Verticle('')
        possible_end = []
        for inode in node.children:
            if inode.type == 'block':
                self.children_visitor(inode)
                possible_end.append(self.end_verticle)
            if inode.type == 'except_clause':
                self.end_verticle = begin_verticle
                self.block_visitor(inode)
                possible_end.append(self.end_verticle)
            if inode.type == 'else_clause':
                self.end_verticle = begin_verticle
                self.block_visitor(inode)
                possible_end.append(self.end_verticle)
        for iend in possible_end:
            if self.edge is None:
                continue
            self.edge.link_verticles(iend, final_verticle)
        self.end_verticle = final_verticle

    def linear_statement_visitor(self, node):
        if self.edge == None:
            return
        line_start = node.start_point[0] + 1
        name = 'simple:{}'.format(line_start)
        sim_verticle = Verticle(name)
        self.add_to_path(sim_verticle)

    def while_statement_visitor(self, node):
        if self.edge == None:
            return
        line_start = node.start_point[0] + 1
        name = 'while:{}'.format(line_start)
        while_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = while_verticle
        else:
            self.add_to_path(while_verticle)
        self.compound_statement_vistor(node)
        if self.edge == None:
            return
        final_verticle = Verticle('')
        self.edge.link_verticles(self.end_verticle, final_verticle)
        self.edge.link_verticles(while_verticle, final_verticle)

    def for_statement_visitor(self, node):
        if self.edge == None:
            return
        line_start = node.start_point[0] + 1
        name = 'for:{}'.format(line_start)
        for_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = for_verticle
        else:
            self.add_to_path(for_verticle)
        self.compound_statement_vistor(node)
        if self.edge == None:
            return
        final_verticle = Verticle('')
        self.edge.link_verticles(self.end_verticle, final_verticle)
        self.edge.link_verticles(for_verticle, final_verticle)
        self.end_verticle = final_verticle

    def preproc_function_def_visitor(self, node):
        # TODO: Add preproc support
        for inode in node.children:
            pass
