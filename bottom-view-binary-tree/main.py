from collections import deque
import sys


# using hashmap
def bottomViewV2(root):
    def f(node, d, hd, level):
        if node == None:
            return

        if (hd not in d) or (d[hd][1] <= level):
            d[hd] = [node.data, level]

        f(node.left, d, hd-1, level+1)
        f(node.right, d, hd+1, level+1)

    # dict with {horizontal distance: (node data, level of node)}
    d = {}
    f(root, d, 0, 0)
    # return values sorted by key
    return [d[k][0] for k in sorted(d.keys())]


# using queue
def bottomViewV1(root):
    if root == None:
        return []

    q = deque()
    q.append([root, 0])

    # dict with {horizontal distance: node data}
    d = {}
    while len(q) > 0:
        node, hd = q.popleft()

        d[hd] = node.data

        if node.left != None:
            q.append([node.left, hd-1])
        if node.right != None:
            q.append([node.right, hd+1])

    # return values sorted by key
    return [d[k] for k in sorted(d.keys())]


def bottomView(root):
    # return bottomViewV2(root)
    return bottomViewV1(root)


# ---------------------------
sys.setrecursionlimit(50000)


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        input()
        s = input()
        root = buildTree(s)
        res = bottomView(root)
        print(*res)
