k = 2


class Node:
    def __init__(self, arr):
        self.point = arr[:k]
        self.left = None
        self.right = None


def insertRec(root, point, depth):
    if not root:
        return Node(point)

    cd = depth % k

    if point[cd] < root.point[cd]:
        root.left = insertRec(root.left, point, depth + 1)
    else:
        root.right = insertRec(root.right, point, depth + 1)

    return root


def insert(root, point):
    return insertRec(root, point, 0)


def arePointsSame(point1, point2):
    return point1[:k] == point2[:k]


def searchRec(root, point, depth):
    if not root:
        return False

    if arePointsSame(root.point, point):
        return True

    cd = depth % k

    if point[cd] < root.point[cd]:
        return searchRec(root.left, point, depth + 1)
    else:
        return searchRec(root.right, point, depth + 1)


def search(root, point):
    return searchRec(root, point, 0)


def findMinRec(root, d, depth):
    if not root:
        return float('inf')

    cd = depth % k

    if cd == d:
        if not root.left:
            return root.point[d]
        else:
            return min(root.point[d], findMinRec(root.left, d, depth + 1))

    return min(
        root.point[d],
        findMinRec(root.left, d, depth + 1),
        findMinRec(root.right, d, depth + 1)
    )


def findMin(root, d):
    return findMinRec(root, d, 0)


def minNode(x, y, z, d):
    res = x
    if y and y.point[d] < res.point[d]:
        res = y
    if z and z.point[d] < res.point[d]:
        res = z
    return res


def findMinNodeRec(root, d, depth):
    if not root:
        return None

    cd = depth % k

    if cd == d:
        if not root.left:
            return root
        else:
            return findMinNodeRec(root.left, d, depth+1)

    return minNode(
        root,
        findMinNodeRec(root.left, d, depth+1),
        findMinNodeRec(root.right, d, depth+1),
        d
    )


def findMinNode(root, d):
    return findMinNodeRec(root, d, 0)


def deleteNodeRec(root, point, depth):
    if not root:
        return None

    cd = depth % k

    if arePointsSame(root.point, point):
        if root.right:
            mini = findMinNode(root.right, cd)
            root.point = mini.point[:k]
            root.right = deleteNodeRec(root.right, mini.point, depth + 1)
        elif root.left:
            mini = findMinNode(root.left, cd)
            root.point = min.point[:k]
            root.right = deleteNodeRec(root.left, mini.point, depth + 1)
        else:
            del root
            return None

        return root

    if point[cd] < root.point[cd]:
        root.left = deleteNodeRec(root.left, point, depth)
    else:
        root.right = deleteNodeRec(root.right, point, depth)


def deleteNode(root, point):
    return deleteNodeRec(root, point, 0)


# search
root = None
points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7],  [10, 19]]

for p in points:
    root = insert(root, p)

point1 = [10, 19]
assert search(root, point1) == True

point2 = [12, 19]
assert search(root, point2) == False


# find minimum
root = None
points = [[30, 40], [5, 25], [70, 70], [10, 12], [50, 30], [35, 45]]

for p in points:
    root = insert(root, p)

assert 5 == findMin(root, 0)
assert 12 == findMin(root, 1)

# delete
root = None
points = [[30, 40], [5, 25], [70, 70], [10, 12], [50, 30], [35, 45]]

for p in points:
    root = insert(root, p)

root = deleteNode(root, points[0])

assert [root.point[0], root.point[1]] == [35, 45]
