class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

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

    def FordFulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.BFS(source, sink, parent):
            flow = float("inf")
            s = sink
            while s != source:
                flow = min(flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = parent[v]

        return max_flow


class Solution:
    def solve(self, N, M, Edges):
        graph = [[0] * N for _ in range(N)]
        for u, v, flow in Edges:
            graph[u-1][v-1] += flow
            graph[v-1][u-1] += flow

        g = Graph(graph)

        source = 0
        sink = N-1
        return g.FordFulkerson(source, sink)


# -----------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N, M = map(int, input().strip().split())
        Edges = []
        input_line = list(map(int, input().strip().split()))
        for i in range(M):
            Edges.append(
                [input_line[3*i], input_line[3*i+1], input_line[3*i+2]])

        ob = Solution()
        ans = ob.solve(N, M, Edges)
        print(ans)
