class Node:
    name: str = ""
    edges: list[tuple[str, str]] = []

    def __init__(self, name):
        self.name = name

    def listEdges(self):
        for i in self.edges:
            print(self.edges[i])


class Edge:
    edge = ()

    def __init__(self, a, b):
        self.edge(a, b)
