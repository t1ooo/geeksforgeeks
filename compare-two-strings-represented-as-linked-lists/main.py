def compare(a, b):
    if a == None and b == None:
        return 0

    if a != None and b == None:
        return 1

    if a == None and b != None:
        return -1

    if a.data > b.data:
        return 1

    if a.data < b.data:
        return -1

    return compare(a.next, b.next)


def compareV2(a, b):
    while a != None and b != None:
        if a.data > b.data:
            return 1
        if a.data < b.data:
            return -1
        a = a.next
        b = b.next

    if a != None and b == None:
        return 1

    if a == None and b != None:
        return -1

    return 0


def compareV1(a, b):
    while a != None and b != None and a.data == b.data:
        a = a.next
        b = b.next

    if a == None and b == None:
        return 0

    if a != None and b == None:
        return 1

    if a == None and b != None:
        return -1

    if a.data > b.data:
        return 1
    else:
        return -1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        input()

        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        n2 = int(input())
        arr2 = input().split()
        ll2 = Llist()
        tail = None
        for nodeData in arr2:
            tail = ll2.insert(nodeData, tail)

        print(compare(ll1.head, ll2.head))
