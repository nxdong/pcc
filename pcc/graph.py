from collections import defaultdict
import json


class Verticle(object):
    def __init__(self, name):
        self.name = name


class Edge(object):
    """the edge_verticle dictionary records the verticles and edges of the python file.
        keys of edge_verticle are all the verticles.
        value of each key represents all the possible next verticles of the key.
    """

    def __init__(self, filename, name, lineno, column):
        self.name = name
        self.edge_verticle = defaultdict(list)
        self.lineno = lineno
        self.column = column
        self.filename = filename

    def link_verticles(self, v1, v2):
        self.edge_verticle[v1].append(v2)
        self.edge_verticle[v2] = []

    def complexity(self):
        # You can print the edge_verticle dictionary to see the flow graph
        # for key,value in self.edge_verticle.items():
        #     print('key--{}, value--{}'.format(key.name,[i.name for i in value]))
        nodes = len(self.edge_verticle)
        edges = sum([len(i) for i in self.edge_verticle.values()])
        return edges-nodes+2

    def __str__(self) -> str:
        return json.dumps({
            'name': self.name,
            'lineno': self.lineno,
            'column': self.column,
            'complexity': self.complexity(),
            'file': self.filename
        })

    def __repr__(self) -> str:
        return self.__str__()
