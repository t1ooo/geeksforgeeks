class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.orig_graph = [v.copy() for v in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    def BFS(self, s, t, parent):
        visited = set()
        visited.add(s)

        queue = []
        queue.append(s)

        while len(queue) > 0:
            u = queue.pop(0)
            for i, val in enumerate(self.graph[u]):
                if val > 0 and i not in visited:
                    queue.append(i)
                    visited.add(i)
                    parent[i] = u

        return t in visited

    def DFS(self, graph, s, visited):
        visited.add(s)
        for i in range(len(graph)):
            if graph[s][i] > 0 and i not in visited:
                self.DFS(graph, i, visited)

    def minCut(self, source, sink):
        parent = [-1] * self.ROW

        while self.BFS(source, sink, parent):
            flow = float("inf")
            s = sink
            while s != source:
                flow = min(flow, self.graph[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = parent[v]

        visited = set()
        self.DFS(self.graph, source, visited)

        res = []
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.orig_graph[i][j] > 0  \
                   and i in visited \
                   and j not in visited:
                    res += [i, j]

        if len(res) == 0:
            res = [-1]

        return res


class Solution:
    def minimumCut(self, A, S, T, N):
        g = Graph(A)
        return g.minCut(S, T)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        A = []
        for i in range(N):
            l = list(map(int, input().strip().split()))
            A.append(l)
        S, T = map(int, input().strip().split())
        ob = Solution()
        res = ob.minimumCut(A, S, T, N)
        for each in res:
            print(each, end=" ")
        print()
