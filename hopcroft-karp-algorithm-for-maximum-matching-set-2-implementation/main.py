NIL = 0
INF = float('inf')


class BipGraph:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.adj = [[] for _ in range(m+1)]
        self.dist = []
        self.pairU = []
        self.pairV = []

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def dfs(self, u):
        if u != NIL:
            for v in self.adj[u]:
                if self.dist[self.pairV[v]] == self.dist[u] + 1 \
                        and self.dfs(self.pairV[v]):
                    self.pairV[v] = u
                    self.pairU[u] = v
                    return True

            self.dist[u] = INF
            return False

        return True

    def bfs(self):
        q = []

        for u in range(1, self.m + 1):
            if self.pairU[u] == NIL:
                self.dist[u] = 0
                q.append(u)
            else:
                self.dist[u] = INF

        self.dist[NIL] = INF

        while len(q) > 0:
            u = q.pop(0)
            if self.dist[u] < self.dist[NIL]:
                for v in self.adj[u]:
                    if self.dist[self.pairV[v]] == INF:
                        self.dist[self.pairV[v]] = self.dist[u] + 1
                        q.append(self.pairV[v])

        return self.dist[NIL] != INF

    def hopcroftKarp(self):
        self.pairU = [NIL] * (self.m + 1)
        self.pairV = [NIL] * (self.n + 1)
        self.dist = [0] * (self.m + 1)

        result = 0
        while self.bfs():
            for u in range(1, self.m + 1):
                if self.pairU[u] == NIL and self.dfs(u):
                    result += 1

        return result


g = BipGraph(4, 4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 1)
g.addEdge(3, 2)
g.addEdge(4, 2)
g.addEdge(4, 4)
assert g.hopcroftKarp() == 4
