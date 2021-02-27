from collections import deque, namedtuple


def topViewV4(root):
    DataLevel = namedtuple("DataLevel", ["data", "level"])

    def f(node, d, hd, level):
        if node == None:
            return

        if (hd not in d) or level < d[hd].level:
            d[hd] = DataLevel(node.data, level)

        f(node.left, d, hd-1, level+1)
        f(node.right, d, hd+1, level+1)

    d = {}
    f(root, d, 0, 0)
    return [d[k].data for k in sorted(d.keys())]


def topViewV3(root):
    def append(q, node, hd):
        if node != None:
            q.append([node, hd])

    q = deque()
    append(q, root, 0)

    l, r = 0, 0
    left, right = [], []

    while len(q) > 0:
        node, hd = q.popleft()

        if hd < l:
            left.append(node.data)
            l = hd
        elif hd > r:
            right.append(node.data)
            r = hd

        append(q, node.left, hd-1)
        append(q, node.right, hd+1)

    left.reverse()

    return left + [root.data] + right


def topViewV2(root):
    def append(q, node, hd):
        if node != None:
            q.append([node, hd])

    q = deque()
    append(q, root, 0)

    # store {horizontal distance: node data}
    d = {}
    while len(q) > 0:
        node, hd = q.popleft()

        if hd not in d:
            d[hd] = node.data

        append(q, node.left, hd-1)
        append(q, node.right, hd+1)

    return [d[k] for k in sorted(d.keys())]


def topViewV1(root):
    def append(q, node, hd, level):
        if node != None:
            q.append([node, hd, level])

    DataLevel = namedtuple("DataLevel", ["data", "level"])

    q = deque()
    append(q, root, 0, 0)

    # store {horizontal distance: DataLevel}
    d = {}
    while len(q) > 0:
        node, hd, level = q.popleft()

        if (hd not in d) or level < d[hd].level:
            d[hd] = DataLevel(node.data, level)

        append(q, node.left, hd-1, level+1)
        append(q, node.right, hd+1, level+1)

    return [d[k].data for k in sorted(d.keys())]


def topView(root):
    return topViewV4(root)
    # return topViewV3(root)
    # return topViewV2(root)
    # return topViewV1(root)


# -----------------------
class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def make_tree():
    n = int(input())
    l = list(map(str, input().split()))
    head = None
    q = deque()
    i = 0
    while(n > 0):
        a, b, c = l[i], l[i+1], l[i+2]
        if(not head):
            head = Node(int(a))
            q.append(head)
        pick = q[0]
        q.popleft()
        if(c == "L"):
            pick.left = Node(int(b))
            q.append(pick.left)
        n = n-1
        if(not n):
            break
        a, b, c = l[i+3], l[i+4], l[i+5]
        if(c == "R"):
            pick.right = Node(int(b))
            q.append(pick.right)
        i = i+6
        n = n-1
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        input()
        root = make_tree()
        res = topView(root)
        print(*res)
