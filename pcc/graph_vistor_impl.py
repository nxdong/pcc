from .vistor_abc import ASTVisitorAbstractClass
from .graph import PathNode
from .graph import PathGraph


class PathGraphingAstVisitor(ASTVisitorAbstractClass):
    """ A visitor for a parsed Abstract Syntax Tree which finds executable
        statements.
    """

    def __init__(self):
        super(PathGraphingAstVisitor, self).__init__()
        self.classname = ""
        self.graphs = {}
        self.visitor = self
        self.reset()

    def reset(self):
        self.graph = None
        self.tail = None

    def appendPathNode(self, name):
        if not self.tail:
            return
        pathnode = PathNode(name)
        self.graph.connect(self.tail, pathnode)
        self.tail = pathnode
        return pathnode

    def default(self, node):
        print("Default Call: ", node, " => type:", node.type)
        super().default(node)
        # if isinstance(node, ast.stmt):
        #     self.visitSimpleStatement(node)
        # else:
        #     super().default(node)

    def visit_module(self, node):
        print("visit_module:", node)
        for inode in node.childs:
            self._visit_statement(inode)

    visit_child = visit_module

    def _visit_statement(self, node):
        print("_visit_statement:", node)

        visit_func = getattr(self, 'visit_' + node.type,
                             self._visit_linear_statement)
        return visit_func(node)

    def _visit_linear_statement(self, node):
        print("_visit_linear_statement:", node)
        (line_no, _) = node.start_point
        name = 'simple_statement:{}'.format(line_no)
        self.appendPathNode(name)

    def _visit_block(self, node):
        for inode in node.childs:
            if inode.type == 'block':
                self.visit_child(inode)

    def visit_function_definition(self, node):
        print("Function Define Call!")
        if self.classname:
            entity = '%s%s' % (self.classname, node.name)
        else:
            entity = node.name
        print("entity:", entity)
        (line_no, column_no) = node.start_point
        name = '{}:{}: {}'.format(line_no, column_no, entity)
        if self.graph is not None:
            # closure
            pathnode = self.appendPathNode(name)
            self.tail = pathnode
            self._visit_block(node)
            bottom = PathNode("", look='point')
            self.graph.connect(self.tail, bottom)
            self.graph.connect(pathnode, bottom)
            self.tail = bottom
        else:
            self.graph = PathGraph(name, entity, line_no, column_no)
            pathnode = PathNode(name)
            self.tail = pathnode
            self._visit_block(node)
            self.graphs["%s%s" % (self.classname, node.name)] = self.graph
            self.reset()

    