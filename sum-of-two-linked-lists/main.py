def reverseList(lst):
    prev = None
    curr = lst
    while curr != None:
        old_next = curr.next
        curr.next = prev
        prev = curr
        curr = old_next
    return prev


def reverseListV1(lst):
    if lst == None or lst.next == None:
        return lst
    node = reverseList(lst.next)
    lst.next.next = lst
    lst.next = None
    return node

# --------------------------------------------


def listLen(lst):
    ln = 1
    curr = lst
    while curr != None:
        ln += 1
        curr = curr.next
    return ln

# --------------------------------------------


def addTwoLists(a, b):
    def copyList(lst):
        copy = LinkedList()
        while lst != None:
            copy.insert(lst.data)
            lst = lst.next
        return copy.head

    # inplace add b to a
    def addListsSameLen(a, b):
        if a == None:
            return 0
        rem = addListsSameLen(a.next, b.next)
        num = a.data + b.data + rem
        digit = num % 10
        rem = num // 10
        a.data = digit
        return rem

    def addNum(lst, lst_end, number):
        if lst == lst_end:
            return number
        rem = addNum(lst.next, lst_end, number)
        num = lst.data + rem
        digit = num % 10
        rem = num // 10
        lst.data = digit
        return rem

    def insert(lst, val):
        node = Node(val)
        if lst == None:
            return node
        node.next = lst
        return node

    def appendNum(lst, rem):
        while rem != 0:
            digit = rem % 10
            rem = rem // 10
            lst = insert(lst, digit)
        return lst

    if a == None:
        return b
    if b == None:
        return a

    la = listLen(a)
    lb = listLen(b)

    if la < lb:
        a, b = b, a
        la, lb = lb, la

    a_copy = copyList(a)
    head = a_copy
    while la != lb:
        head = head.next
        la -= 1

    rem = addListsSameLen(head, b)
    if head == a_copy:
        return appendNum(head, rem)

    rem = addNum(a_copy, head, rem)
    return appendNum(a_copy, rem)


def addTwoListsV2(a, b):
    def pad(lst, lstLen, len, val):
        while lstLen != len:
            node = Node(val)
            node.next = lst
            lst = node
            lstLen += 1
        return lst

    def add(a, b):
        if a == None:
            return None, 0
        next, rem = add(a.next, b.next)
        num = a.data + b.data + rem
        digit = num % 10
        rem = num // 10
        curr = Node(digit)
        curr.next = next
        return curr, rem

    la = listLen(a)
    lb = listLen(b)

    if la < lb:
        a, b = b, a
        la, lb = lb, la

    b_padded = pad(b, lb, la, 0)

    lst, rem = add(a, b_padded)
    if rem == 0:
        return lst

    curr = Node(rem)
    curr.next = lst
    return curr


def addTwoListsV1(a, b):
    def insert(lst, val):
        node = Node(val)
        if lst == None:
            return node
        node.next = lst
        return node

    ra = reverseList(a)
    rb = reverseList(b)

    list = None
    rem = 0
    while ra != None and rb != None:
        num = ra.data + rb.data + rem
        digit = num % 10
        rem = num // 10
        list = insert(list, digit)
        ra = ra.next
        rb = rb.next

    while ra != None:
        num = ra.data + rem
        digit = num % 10
        rem = num // 10
        list = insert(list, digit)
        ra = ra.next

    while rb != None:
        num = rb.data + rem
        digit = num % 10
        rem = num // 10
        list = insert(list, digit)
        rb = rb.next

    if rem != 0:
        list = insert(list, rem)

    return list

# --------------------------------------------

# Node Class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head


def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        input()

        n = int(input())
        arr1 = (int(x) for x in input().split())
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        m = int(input())
        arr2 = (int(x) for x in input().split())
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        res = addTwoLists(LL1.head, LL2.head)
        printList(res)
