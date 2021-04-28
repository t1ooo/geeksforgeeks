from collections import deque
import sys

sys.setrecursionlimit(50000)


def LCAv3(root, n1, n2):
    def f(node, n1, n2):
        if node == None:
            return None

        if node.data == n1 or node.data == n2:
            return node

        left = f(node.left, n1, n2)
        right = f(node.right, n1, n2)

        if left != None and right != None:
            return node

        if left != None:
            return left
        else:
            return right

    return f(root, n1, n2)


def LCAv2(root, n1, n2):
    def f(node, n1, n2):
        if node == None:
            return None

        data = node.data

        if n1 < data and n2 < data:
            return f(node.left, n1, n2)

        if data < n1 and data < n2:
            return f(node.right, n1, n2)

        return node

    return f(root, n1, n2)


def LCAv1(root, n1, n2):
    node = root
    while node != None:
        data = node.data

        if n1 < data and n2 < data:
            node = node.left
        elif data < n1 and data < n2:
            node = node.right
        else:
            break

    return node


def LCA(root, n1, n2):
    return LCAv3(root, n1, n2)
    # return LCAv2(root, n1, n2)
    # return LCAv1(root, n1, n2)


# ----------------------


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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
        n1, n2 = list(map(int, input().split()))
        print(LCA(root, n1, n2).data)
