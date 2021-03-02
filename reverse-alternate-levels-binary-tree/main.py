from collections import deque


def reverseAlternateV1(root):
    def store(node, level, datas):
        if node == None:
            return

        if level % 2 == 0:
            if level not in datas:
                datas[level] = []
            datas[level].append(node.data)

        store(node.left, level+1, datas)
        store(node.right, level+1, datas)

    def swap(node, level, datas):
        if node == None:
            return

        if level % 2 == 0:
            node.data = datas[level].pop()

        swap(node.left, level+1, datas)
        swap(node.right, level+1, datas)

    if root != None:
        datas = {}
        store(root, 1, datas)
        swap(root, 1, datas)


def reverseAlternateV2(root):
    def swapNodeDatas(nodes):
        for i in range(len(nodes) // 2):
            a = nodes[i]
            b = nodes[len(nodes) - i - 1]
            a.data, b.data = b.data, a.data

    def append(q, node, level):
        if node != None:
            q.append([node, level])

    q = deque()
    prevLevel = 1
    append(q, root, prevLevel)
    levelNodes = []
    while len(q) > 0:
        node, level = q.popleft()

        if level != prevLevel:
            prevLevel = level
            swapNodeDatas(levelNodes)
            levelNodes = []

        if level % 2 == 0:
            levelNodes.append(node)

        append(q, node.left, level+1)
        append(q, node.right, level+1)

    swapNodeDatas(levelNodes)
    levelNodes = []


def reverseAlternateV3(root):
    def f(left, right, level):
        if left == None or right == None:
            return

        if level % 2 == 0:
            left.data, right.data = right.data, left.data

        f(left.left, right.right, level+1)
        f(left.right, right.left, level+1)

    if root != None:
        f(root.left, root.right, 0)


def reverseAlternate(root):
    # return reverseAlternateV1(root)
    # return reverseAlternateV2(root)
    return reverseAlternateV3(root)

# --------------------------


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


def preorder(root):
    if not root:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        input()
        s = input()
        root = buildTree(s)
        reverseAlternate(root)
        inorder(root)
        print()
