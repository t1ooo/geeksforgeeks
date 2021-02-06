class Solution:
    def kruskalMST(self, V, graph):
        ret = []
        parent = [-1] * V
        graph.sort(key=lambda x: x[2])
        for a, b, _ in graph:
            if not (len(ret) < V - 1):
                break
            parent_a = self.find_parent(parent, a)
            parent_b = self.find_parent(parent, b)
            if parent_a == parent_b:
                continue
            self.union(parent, parent_a, parent_b)
            ret.append([a, b])
        return ret

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, a, b):
        parent_a = self.find_parent(parent, a)
        parent_b = self.find_parent(parent, b)
        parent[parent_a] = parent_b


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        graph_size = int(input().strip())
        edge_count = int(input().strip())
        graph = []
        for _ in range(edge_count):
            a, b, weight = [int(x) for x in input().strip().split(" ")]
            graph.append([a, b, weight])
        s = Solution()
        print(s.kruskalMST(graph_size, graph))
