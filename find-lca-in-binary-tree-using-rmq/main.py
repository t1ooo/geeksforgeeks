from math import log2, floor


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.val_max = self._get_max_val()
        self.euler = [0] * (2 * self.val_max - 1)
        self.level = [0] * (2 * self.val_max - 1)
        self.f_occur = [-1] * (self.val_max + 1)
        self.fill = 0
        self.segment_tree = []

    def _get_max_val(self):
        stack = [self.root]
        max_val = -1

        while stack:
            x = stack.pop()
            if x.val > max_val:
                max_val = x.val

            if x.left:
                stack.append(x.left)
            if x.right:
                stack.append(x.right)

        return max_val

    def rmq_util(self, index, ss, se, qs, qe):
        if qs <= ss and qe >= se:
            return self.segment_tree[index]
        elif se < qs or ss > qe:
            return -1

        mid = (ss + se) // 2

        q1 = self.rmq_util(2 * index + 1, ss, mid, qs, qe)
        q2 = self.rmq_util(2 * index + 2, mid + 1, se, qs, qe)

        if q1 == -1:
            return q2
        if q2 == -1:
            return q1
        return q1 if self.level[q1] < self.level[q2] else q2

    def rmq(self, n, qs, qe):
        if qs < 0 or qe > n - 1 or qs > qe:
            return -1

        return self.rmq_util(0, 0, n - 1, qs, qe)

    def construct_segment_tree_util(self, si, ss, se, arr):
        if ss == se:
            self.segment_tree[si] = ss
        else:
            mid = (ss + se) // 2
            index_left, index_right = si * 2 + 1, si * 2 + 2
            self.construct_segment_tree_util(index_left, ss, mid, arr)
            self.construct_segment_tree_util(index_right, mid+1, se, arr)

            if arr[self.segment_tree[index_left]] < arr[self.segment_tree[index_right]]:
                self.segment_tree[si] = self.segment_tree[index_left]
            else:
                self.segment_tree[si] = self.segment_tree[index_right]

    def construct_segment_tree(self, arr, n):
        x = floor(log2(n) + 1)

        max_size = 2 * pow(2, x) - 1
        self.segment_tree = [0] * max_size

        self.construct_segment_tree_util(0, 0, n - 1, arr)

    def euler_tour(self, node, lev):
        if node:
            self.euler[self.fill] = node.val
            self.level[self.fill] = lev
            self.fill += 1

            if self.f_occur[node.val] == -1:
                self.f_occur[node.val] = self.fill - 1

            if node.left:
                self.euler_tour(node.left, lev + 1)
                self.euler[self.fill] = node.val
                self.level[self.fill] = lev
                self.fill += 1

            if node.right:
                self.euler_tour(node.right, lev + 1)
                self.euler[self.fill] = node.val
                self.level[self.fill] = lev
                self.fill += 1

    def find_lca(self, u, v):
        self.euler_tour(self.root, 0)

        self.construct_segment_tree(self.level, 2 * self.val_max - 1)

        if self.f_occur[u] > self.f_occur[v]:
            u, v = v, u

        qs = self.f_occur[u]
        qe = self.f_occur[v]

        index = self.rmq(2 * self.val_max - 1, qs, qe)

        return self.euler[index]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

tree = BinaryTree(root)
u, v = 4, 9
assert tree.find_lca(u, v) == 2
