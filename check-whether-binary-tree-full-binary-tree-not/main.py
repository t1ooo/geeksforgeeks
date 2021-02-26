from collections import deque


def isFullTreeV1(root):
    def f(node):
        if node == None:
            return True
        if node.left == None and node.right != None:
            return False
        if node.left != None and node.right == None:
            return False
        return f(node.left) and f(node.right)

    return f(root)


def isFullTreeV2(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()

        if node == None:
            continue
        if node.left == None and node.right != None:
            return False
        if node.left != None and node.right == None:
            return False

        q.append(node.left)
        q.append(node.right)

    return True


def isFullTreeV3(root):
    def append(q, node):
        if node != None:
            q.append(node)

    q = deque()
    append(q, root)
    while len(q) > 0:
        node = q.popleft()

        if node.left == None and node.right != None:
            return False
        if node.left != None and node.right == None:
            return False

        append(q, node.left)
        append(q, node.right)

    return True


def isFullTree(root):
    return isFullTreeV3(root)
    # return isFullTreeV2(root)
    # return isFullTreeV1(root)


# ------------------------


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
        if isFullTree(root):
            print(1)
        else:
            print(0)
