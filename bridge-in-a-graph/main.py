class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.Time = 0

    def addEdge(self, u, v):
        self._addEdge(u, v)
        self._addEdge(v, u)

    def _addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def visit(self, u, visited, low, disc, parent, res):
        visited.add(u)
        low[u] = self.Time
        disc[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if v not in visited:
                parent[v] = u
                self.visit(v, visited, low, disc, parent, res)
                if low[v] > disc[u]:
                    res.append([u, v])
                low[u] = min(low[u], low[v])
            elif parent[u] != v:
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = set()
        low = [float('inf')] * self.V
        disc = [float('inf')] * self.V
        parent = [-1] * self.V
        res = []

        for i in range(self.V):
            if i not in visited:
                self.visit(i, visited, low, disc, parent, res)

        return res


def print_bridges(bridges):
    for edge in bridges:
        print(" ".join([str(vertex) for vertex in edge]))


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("Bridges in first graph")
print_bridges(g1.bridge())

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("Bridges in second graph")
print_bridges(g2.bridge())

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("Bridges in third graph")
print_bridges(g3.bridge())
