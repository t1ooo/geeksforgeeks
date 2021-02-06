# User function Template for python3

def print_adj(adj):
    print(adj)
    for k, v in enumerate(adj):
        for vv in v:
            print(k, "-->", vv[0], " = ", vv[1])


class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list
    '''
    def spanningTree(self, V, adj):
        # print(adj)
        key = [float('inf')] * V
        key[0] = 0
        mstSet = set()
        for _ in range(V):
            mk = self.minKey(key, mstSet)
            mstSet.add(mk)
            for a in adj[mk]:
                v, weight = a
                if key[v] > weight and (v not in mstSet):
                    key[v] = weight
        return sum(key)

    def minKey(self, key, mstSet):
        min = float('inf')
        min_index = -1
        for i, v in enumerate(key):
            if min > v and (i not in mstSet):
                min = v
                min_index = i
        return min_index


# naive solution
class SolutionV1:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list
    '''
    def spanningTree(self, V, adj):
        # print(adj)
        cost = 0
        nodeSet = set([0])
        while len(nodeSet) < V:
            min_weight, min_node = self.find_min_weight(adj, nodeSet)
            nodeSet.add(min_node)
            # print(nodeSet, min_weight)
            cost += min_weight
        return cost

    def find_min_weight(self, adj, nodeSet):
        min_weight = float('inf')
        min_node = None
        for i in nodeSet:
            for vv in adj[i]:
                node, weight = vv
                # print(i, node, '-->', weight)
                if (node not in nodeSet) and min_weight > weight:
                    min_weight = weight
                    min_node = node
        return (min_weight, min_node)

# {
#  Driver Code Starts
# Initial Template for Python 3


# Contributed by : Nagendra Jha
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
# } Driver Code Ends
