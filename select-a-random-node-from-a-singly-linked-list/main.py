import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def selectRandom(self):
        if self.head == None:
            raise Exception("list is empty")

        return self.selectRandomN(1)[0]

    # Reservoir Sampling
    def selectRandomN(self, k):
        selected = []

        curr = self.head
        while curr != None and len(selected) < k:
            selected.append(curr.data)
            curr = curr.next

        random.seed()

        i = k+1
        while curr != None:
            j = random.randrange(0, i+1)
            if j < k:
                selected[j] = curr.data
            curr = curr.next
            i += 1

        return selected

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# Driver program to test above function
list = LinkedList()
list.push(5)
list.push(30)
list.push(3)
list.push(50)

print("random element: ", list.selectRandom())
print("random 0 elements: ", list.selectRandomN(0))
print("random 3 elements: ", list.selectRandomN(3))
print("random 10 elements (10 > len(list)): ", list.selectRandomN(10))
