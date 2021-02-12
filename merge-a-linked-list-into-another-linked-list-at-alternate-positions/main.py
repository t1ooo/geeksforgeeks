# 1->2->3
# 4->5->6->7->8
#
# 1->4->2->5->3->6
# 7->8
def mergeList(head1, head2):
    a = head1
    b = head2
    while a != None and b != None:
        a_next = a.next
        b_next = b.next

        b.next = a.next
        a.next = b

        a = a_next
        b = b_next

    return [head1, b]


# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        head = mergeList(head1, head2)
        printList(head[0])
        printList(head[1])
