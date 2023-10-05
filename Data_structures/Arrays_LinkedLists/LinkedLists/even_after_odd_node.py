class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return 

        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)

        return 
    
numList = [1, 2, 3, 4, 5, 6]

linkedList = LinkedList()

for e in numList:
    linkedList.append(e)

node = linkedList.head

while node:
    print(node.value)
    node = node.next