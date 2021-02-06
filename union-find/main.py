class Solution:
    def isCyclic(self, size, graph):
        parent = [-1] * size
        for a, b in graph:
            parent_a = self.find_parent(parent, a)
            parent_b = self.find_parent(parent, b)
            if parent_a == parent_b:
                return True
            self.union(parent, parent_a, parent_b)
        return False

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, a, b):
        parent_a = self.find_parent(parent, a)
        parent_b = self.find_parent(parent, b)
        parent[parent_a] = parent_b


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        graph_size = int(input().strip())
        edge_size = int(input().strip())
        graph = []
        for _ in range(edge_size):
            row = [int(x) for x in input().strip().split(' ')]
            graph.append(row)
        s = Solution()
        print(s.isCyclic(graph_size, graph))
