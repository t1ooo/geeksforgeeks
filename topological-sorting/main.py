class Solution:
    def topoSort(self, size, graph):
        ret = []
        visited = set()
        for i in range(size):
            if i not in visited:
                self.traversal(i, graph, visited, ret)
        ret.reverse()
        return ret

    def traversal(self, i, graph, visited, ret):
        visited.add(i)
        for v in graph[i]:
            if v not in visited:
                self.traversal(v, graph, visited, ret)
        ret.append(i)


import sys
sys.setrecursionlimit(10**6)


def check(graph, N, res):
    map = [0]*N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        delim = input()

        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()
        res = ob.topoSort(N, adj)
        if check(adj, N, res):
            print(1)
        else:
            print(0)
