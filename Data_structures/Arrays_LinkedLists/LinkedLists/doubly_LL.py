class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            return 

        else:
            self.tail.next = Node(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

        return 

linked_list = DoublyLinkedList()
input_list = [1, 2, 3, 4]

for e in input_list:
    linked_list.append(e)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

node = linked_list.tail
while node:
    print(node.value)
    node = node.previous