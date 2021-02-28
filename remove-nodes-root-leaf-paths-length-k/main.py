def removeShortPathNodes(root, k):
    def f(root, level, k):
        if root == None:
            return None

        if level >= k:
            return root

        if root.left == None and root.right == None:
            return None

        root.left = f(root.left, level + 1, k)
        root.right = f(root.right, level + 1, k)

        return root

    return f(root, 1, k)


# --------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.right.right = Node(6)
    root.right.right.left = Node(8)
    k = 4
    res = removeShortPathNodes(root, k)
    printInorder(res)
