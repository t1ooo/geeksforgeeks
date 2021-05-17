import copy
from typing import Optional


class Interval:
    low: int
    hight: int

    def __init__(self, low: int, hight: int) -> None:
        self.low = low
        self.hight = hight

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Interval)
            and self.low == other.low
            and self.hight == other.hight
        )


class Node:
    i: Interval
    max: int
    left: Optional["Node"]
    right: Optional["Node"]

    def __init__(self, i: Interval) -> None:
        self.i = copy.deepcopy(i)
        self.max = i.hight
        self.left = None
        self.right = None


def insert(root: Optional["Node"], i: Interval) -> Node:
    if not root:
        return Node(i)

    if i.low < root.i.low:
        root.left = insert(root.left, i)
    else:
        root.right = insert(root.right, i)

    root.max = max(root.max, i.hight)

    return root


def isOverlap(a: Interval, b: Interval) -> bool:
    return a.low <= b.low and b.hight <= a.hight


def searchOverlap(root: Optional[Node], i: Interval) -> Optional[Interval]:
    if not root:
        return None

    if isOverlap(root.i, i):
        return root.i

    if root.left and root.left.max >= i.low:
        return searchOverlap(root.left, i)

    return searchOverlap(root.right, i)


ints = [[15, 20], [10, 30], [17, 18], [5, 20], [12, 15], [30, 40]]
root = None
for low, hight in ints:
    root = insert(root, Interval(low, hight))

x = Interval(6, 7)
assert searchOverlap(root, x) == Interval(5, 20)
