def sortedInsert(head, key):
    if head == None or key < head.data:
        insert = Node(key)
        insert.next = head
        return insert
    else:
        insert = sortedInsert(head.next, key)
        head.next = insert
        return head


def sortedInsertV2(head, key):
    insert = Node(key)
    curr = head
    prev = None
    while curr != None:
        if insert.data < curr.data:
            break
        prev = curr
        curr = curr.next

    insert.next = curr
    if prev == None:
        return insert

    prev.next = insert
    return head


def sortedInsertV1(head, key):
    insert = Node(key)

    if head == None:
        return insert

    if insert.data < head.data:
        insert.next = head
        return insert

    curr = head
    next = head.next
    while next != None:
        if insert.data < next.data:
            break
        curr = next
        next = next.next

    curr.next = insert
    insert.next = next
    return head

# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev = self.head

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        input()

        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)

        key = int(input())
        h = sortedInsert(a.head, key)
        printList(h)

# } Driver Code Ends
