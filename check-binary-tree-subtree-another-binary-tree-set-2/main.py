import sys
from collections import deque


# geeksforgeeks.org: maximum recursion depth exceeded in comparison
# leetcode.com: Wrong Answer
def isSubTreeV1(T, S):
    def f(tree, subtree, treeOffset):
        if tree == None and subtree == None:
            return True

        elif tree == None:
            return False

        elif subtree == None or tree.data != subtree.data:
            subtree = S  # reset
            for nextTreeOffset in [treeOffset.left, treeOffset.right]:
                tree = nextTreeOffset
                if f(tree, subtree, nextTreeOffset):
                    return True

            return False

        # s.data == st.data
        else:
            left = f(tree.left, subtree.left, treeOffset)
            right = f(tree.right, subtree.right, treeOffset)
            return right and left

    return f(T, S, T)


# geeksforgeeks.org: maximum recursion depth exceeded in comparison
# leetcode.com: Accepted
def isSubTreeV2(T, S):
    def isIdentical(root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False

        return (
            root1.data == root2.data and
            isIdentical(root1.left, root2.left) and
            isIdentical(root1.right, root2.right)
        )

    def isSubtree(T, S):
        if S == None:
            return True

        if T == None:
            return False

        if isIdentical(T, S):
            return True

        return isSubtree(T.left, S) or isSubtree(T.right, S)

    return isSubtree(T, S)


# geeksforgeeks.org: maximum recursion depth exceeded in comparison
# leetcode.com: Accepted
def isSubTreeV3(T, S):
    def inOrder(node, res):
        if node == None:
            res.append(None)
            return

        inOrder(node.left, res)
        res.append(node.data)
        inOrder(node.right, res)

    def preOrder(node, res):
        if node == None:
            res.append(None)
            return

        res.append(node.data)
        preOrder(node.left, res)
        preOrder(node.right, res)

    def isSublist(lst, sublst):
        l = 0
        l_start = 0
        s = 0
        while l < len(lst) and s < len(sublst):
            if lst[l] == sublst[s]:
                l += 1
                s += 1
            else:
                l_start += 1
                l = l_start
                s = 0

        return s == len(sublst)

    t = []
    s = []
    inOrder(T, t)
    inOrder(S, s)
    a = isSublist(t, s)

    t = []
    s = []
    preOrder(T, t)
    preOrder(S, s)
    b = isSublist(t, s)

    return a and b


# v5 without recursion
# geeksforgeeks.org: Time Limit Exceeded
# leetcode.com: Accepted
def isSubTreeV4(T, S):
    def inOrder(node, res):
        s = []
        while len(s) > 0:  # or node ≠ null)
            if node != None:
                s.append(node)
                node = node.left
            else:
                res.append(None)  # special case for empty node
                node = s.pop()
                res.append(node.data)
                node = node.right

    def preOrder(node, res):
        s = []
        s.append(node)
        while len(s) > 0:
            node = s.pop()
            if node == None:
                res.append(None)  # special case for empty node
                continue
            res.append(node.data)
            s.append(node.right)
            s.append(node.left)

    def isSublist(lst, sublst):
        l = 0
        l_start = 0
        s = 0
        while l < len(lst) and s < len(sublst):
            if lst[l] == sublst[s]:
                l += 1
                s += 1
            else:
                l_start += 1
                l = l_start
                s = 0

        return s == len(sublst)

    t = []
    s = []
    inOrder(T, t)
    inOrder(S, s)
    a = isSublist(t, s)

    t = []
    s = []
    preOrder(T, t)
    preOrder(S, s)
    b = isSublist(t, s)

    return a and b


# geeksforgeeks.org: Correct Answer
# leetcode.com: Accepted
def isSubTreeV5(T, S):
    def inOrder(node, res):
        s = []
        while len(s) > 0:  # or node ≠ null)
            if node != None:
                s.append(node)
                node = node.left
            else:
                res.append("$")  # special case for empty node
                node = s.pop()
                res.append("#"+str(node.data))
                node = node.right

    def preOrder(node, res):
        s = []
        s.append(node)
        while len(s) > 0:
            node = s.pop()
            if node == None:
                res.append("$")  # special case for empty node
                continue
            res.append("#"+str(node.data))
            s.append(node.right)
            s.append(node.left)

    def isSublist(lst, sublst):
        return "".join(sublst) in "".join(lst)

    t = []
    s = []
    inOrder(T, t)
    inOrder(S, s)
    a = isSublist(t, s)

    t = []
    s = []
    preOrder(T, t)
    preOrder(S, s)
    b = isSublist(t, s)

    return a and b


# geeksforgeeks.org: maximum recursion depth exceeded in comparison
# leetcode.com: Accepted
def isSubTreeV6(t, s):
    def traverse(node):
        if not node:
            return None
        # return f"#{node.data} {traverse(node.left)} {traverse(node.right)}"
        return "#%s %s %s" % (node.data, traverse(node.left), traverse(node.right))

    return traverse(s) in traverse(t)


# geeksforgeeks.org: Correct Answer
# leetcode.com: Accepted
def isSubTreeV7(t, s):
    def traverse(node):
        s = [node]
        res = ""
        while len(s) > 0:
            node = s.pop()
            if not node:
                res += "$"
                continue
            res += "#" + str(node.data)
            s.append(node.left)
            s.append(node.right)
        return res

    return traverse(s) in traverse(t)


def isSubTree(T, S):
    sys.setrecursionlimit(15000)
    try:
        # return isSubTreeV1(T, S)
        # return isSubTreeV2(T, S)
        # return isSubTreeV3(T, S)
        # return isSubTreeV4(T, S)
        # return isSubTreeV5(T, S)
        # return isSubTreeV6(T, S)
        return isSubTreeV7(T, S)
    except Exception as e:
        print(e)


# ------------------------------
# sys.setrecursionlimit(1000000)
sys.setrecursionlimit(10000)


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
        rootT = buildTree(input())
        rootS = buildTree(input())
        if isSubTree(rootT, rootS) is True:
            print("1")
        else:
            print("0")
