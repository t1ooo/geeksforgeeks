# in   25 15 4 14 13 23
#      16 3 24 14 1 25 10
#
# out  25 14

# use hashing
def findIntersection(head1, head2):
    s = set()
    while head2 != None:
        s.add(head2.data)
        head2 = head2.next

    list = linkedList()
    while head1 != None:
        if head1.data in s:
            list.insert(head1.data)
        head1 = head1.next

    return list.head


# use merge sort (does not preserve order)
def findIntersectionV2(head1, head2):
    def mergeSortedLists(a, b):
        list = linkedList()
        while a != None and b != None:
            if a.data <= b.data:
                list.insert(a.data)
                a = a.next
            elif a.data > b.data:
                list.insert(b.data)
                b = b.next

        while a != None:
            list.insert(a.data)
            a = a.next

        while b != None:
            list.insert(b.data)
            b = b.next

        return list.head

    # def middleOfList(lst):
    #     slow = lst
    #     fast = lst
    #     while fast != None and fast.next != None:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow

    def splitList(lst):
        slow_prev = None
        slow = lst
        fast = lst
        while fast != None and fast.next != None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        slow_prev.next = None
        return lst, slow

    # merge sort
    def sortList(lst):
        if lst == None or lst.next == None:
            return lst
        left, right = splitList(lst)
        left = sortList(left)
        right = sortList(right)
        return mergeSortedLists(left, right)

    if head1 == None:
        return None
    if head2 == None:
        return None

    a = sortList(head1)
    b = sortList(head2)

    list = linkedList()
    while a != None and b != None:
        if a.data == b.data:
            list.insert(a.data)
            a = a.next
            b = b.next
        elif a.data > b.data:
            b = b.next
        elif a.data < b.data:
            a = a.next

    return list.head


# simple
def findIntersectionV1(head1, head2):
    def contains(lst, val):
        while lst != None:
            if lst.data == val:
                return True
            lst = lst.next
        return False

    list = linkedList()
    while head1 != None:
        if contains(head2, head1.data):
            list.insert(head1.data)
        head1 = head1.next

    return list.head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)

        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)

        result = findIntersection(ll1.head, ll2.head)
        printList(result)
