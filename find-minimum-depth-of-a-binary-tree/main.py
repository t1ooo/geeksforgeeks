import sys
from collections import deque

MAX = float("inf")


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# a node is a leaf node if both left and right child nodes of it are NULL
def isLeafNode(node):
    return node.left == None and node.right == None


def minDepthRec(root):
    def f(node):
        if node == None:
            return MAX
        if isLeafNode(node):
            return 1
        return 1 + min(
            f(node.left),
            f(node.right)
        )

    if root == None:
        return 0
    else:
        return f(root)


def minDepthRecV2(root):
    def f(node):
        if node == None:
            return 0
        if isLeafNode(node):
            return 1
        if node.left == None:
            return 1 + f(node.right)
        if node.right == None:
            return 1 + f(node.left)
        return 1 + min(
            f(node.left),
            f(node.right)
        )

    return f(root)


def minDepthRecAcc(root):
    def f(node, h):
        if node == None:
            return MAX
        if isLeafNode(node):
            return h+1
        return min(
            f(node.left, h+1),
            f(node.right, h+1)
        )

    if root == None:
        return 0
    else:
        return f(root, 0)


def minDepthQueue(root):
    if root == None:
        return 0

    h = 1
    q = deque()
    q.append([root, h])

    while len(q) > 0:
        node, h = q.popleft()

        if isLeafNode(node):
            break

        if node.left != None:
            q.append([node.left, h+1])
        if node.right != None:
            q.append([node.right, h+1])

    return h


def minDepth(root):
    # return minDepthRec(root)
    # return minDepthRecV2(root)
    # return minDepthRecAcc(root)
    return minDepthQueue(root)


# ------------------------------


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
        print(minDepth(root))
