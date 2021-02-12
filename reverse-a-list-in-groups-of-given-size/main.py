# 5 9  9 3  5 6  6 2  8 2 | 2
# 9 5  3 9  6 5  2 6  2 8
def reverse(head, k):
    if head == None:
        return head

    i = 0
    prev = None
    curr = head
    while curr != None and i < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1

    head.next = reverse(curr, k)

    return prev


def reverseV1(head, k):
    def reverseList(head, tail):
        prev = None
        curr = head
        while curr != tail:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    ret_head = None
    prev_chunk_tail_rev = None
    chunk_head = head
    i = 1
    while head != None:
        next = head.next
        if i % k == 0 or next == None:
            chunk_tail = next
            chunk_head_rev = reverseList(chunk_head, chunk_tail)

            if prev_chunk_tail_rev != None:
                prev_chunk_tail_rev.next = chunk_head_rev
            prev_chunk_tail_rev = chunk_head

            chunk_head = chunk_tail

            if ret_head == None:
                ret_head = chunk_head_rev

        head = next
        i += 1

    return ret_head


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        input()
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
