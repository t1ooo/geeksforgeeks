class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


class Value:
    def __init__(self, val):
        self.val = val


def last(arr):
    return arr[len(arr)-1]


def constructTreeV4(arr, size):
    if size == 0:
        return None

    root = Node(arr[0])
    s = [root]

    for data in arr[1:]:
        node = Node(data)

        temp = None
        while len(s) > 0 and data > last(s).data:
            temp = s.pop()

        if temp == None:
            temp = last(s)
            temp.left = node
        else:
            temp.right = node

        s.append(node)

    return root


def constructTreeV3(arr, size):
    def insert(arr, i, size, min, max):
        if not (i.val < size):
            return None

        data = arr[i.val]
        if data < min or max < data:
            return None

        i.val += 1
        node = Node(data)
        node.left = insert(arr, i, size, min, data)
        node.right = insert(arr, i, size, data+1, max)
        return node

    i = Value(0)
    tree = insert(arr, i, size, float("-inf"), float("inf"))
    return tree


# loop insert
def constructTreeV2(arr, size):
    def insert(root, val):
        prev = root
        curr = root
        while curr != None:
            prev = curr
            if val <= curr.data:
                curr = curr.left
            else:
                curr = curr.right

        new = Node(val)
        if prev == None:
            return new

        if val <= prev.data:
            prev.left = new
        else:
            prev.right = new

        return root

    tree = None
    for v in arr:
        tree = insert(tree, v)
    return tree


# rec insert
def constructTreeV1(arr, size):
    def insert(node, val):
        if node == None:
            return Node(val)

        if val <= node.data:
            node.left = insert(node.left, val)
        else:
            node.right = insert(node.right, val)

        return node

    tree = None
    for v in arr:
        tree = insert(tree, v)
    return tree


def constructTree(arr, size):
    return constructTreeV4(arr, size)
    # return constructTreeV3(arr, size)
    # return constructTreeV2(arr, size)
    # return constructTreeV1(arr, size)


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        input()
        size = int(input())
        pre = [int(x)for x in input().split()]
        root = constructTree(pre, size)
        postOrd(root)
        print()
