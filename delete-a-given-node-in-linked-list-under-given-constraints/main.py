# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def deleteNode(self, data):
        if self.head == None:
            return

        prev = None
        curr = self.head
        while curr != None:
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        if prev == None:
            self.head = curr.next
            return

        prev.next = curr.next


llist = LinkedList()
llist.push(3)
llist.push(2)
llist.push(6)
llist.push(5)
llist.push(11)
llist.push(10)
llist.push(15)
llist.push(12)

print("Given Linked List: ")
llist.print()
print()

print("Deleting node 10:")
llist.deleteNode(10)
llist.print()
print()

print("Deleting first node:")
llist.deleteNode(12)
llist.print()
print()

print("Deleting last node:")
llist.deleteNode(3)
llist.print()
print()
