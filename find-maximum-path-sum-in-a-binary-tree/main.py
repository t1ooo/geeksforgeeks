from collections import deque


class MaxTop:
    def __init__(self, val=float("-inf")):
        self.val = val


def findMaxSumV1(root):
    def f(node, max_top):
        if node == None:
            return 0

        left = f(node.left, max_top)
        right = f(node.right, max_top)
        data = node.data

        max_single = max(
            data,
            data + left,
            data + right,
        )

        max_top.val = max(
            max_top.val,
            max_single,
            data + left + right,
        )

        return max_single

    max_top = MaxTop()
    f(root, max_top)
    return max_top.val


def findMaxSumV2(root):
    def f(node, max_top):
        if node == None:
            return 0

        left = max(0, f(node.left, max_top))
        right = max(0, f(node.right, max_top))

        max_top.val = max(max_top.val, node.data + left + right)

        return node.data + max(left, right)

    max_top = MaxTop()
    f(root, max_top)
    return max_top.val


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ----------------------------
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
m = 42


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.left.left = Node(2)
root.left.right = Node(0)
root.right.right = Node(0)
root.right.right.left = Node(0)
root.right.right.right = Node(0)
m = 3


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(0)
root.left = Node(0)
root.right = Node(0)
root.left.left = Node(0)
root.left.right = Node(0)
root.right.right = Node(1)
root.right.right.left = Node(2)
root.right.right.right = Node(3)
m = 6


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.left.left = Node(2)
root.left.right = Node(3)
root.right.right = Node(0)
root.right.right.left = Node(0)
root.right.right.right = Node(0)
m = 6


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)
m = 25


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.right = Node(3)
root.right.right.left = Node(1)
root.right.right.right = Node(2)
m = 13


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(1)
root.left = Node(-2)
root.right = Node(-3)
root.left.left = Node(-4)
root.left.right = Node(-5)
root.right.right = Node(-6)
root.right.right.left = Node(-7)
root.right.right.right = Node(-8)
m = 1


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(0)
root.left.right = Node(0)
root.right.right = Node(10)
root.right.right.left = Node(20)
root.right.right.right = Node(30)
m = 60


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(-100)
root.left = Node(0)
root.right = Node(0)
root.left.left = Node(0)
root.left.right = Node(0)
root.right.right = Node(10)
root.right.right.left = Node(-20)
root.right.right.right = Node(-30)
m = 10


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(-100)
root.left = Node(50)
root.right = Node(0)
root.left.left = Node(0)
root.left.right = Node(0)
root.right.right = Node(10)
root.right.right.left = Node(20)
root.right.right.right = Node(30)
m = 60


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"

# ----------------------------
root = Node(-100)
root.left = Node(-100)
root.right = Node(-100)
root.left.left = Node(-100)
root.left.right = Node(-100)
root.right.right = Node(-10)
root.right.right.left = Node(-20)
root.right.right.right = Node(-30)
m = -10


msum = findMaxSumV1(root)
assert msum == m, f"{msum} == {m}"

msum = findMaxSumV2(root)
assert msum == m, f"{msum} == {m}"
