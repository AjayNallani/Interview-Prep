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
    
    def reverse(self):
        previousNode, currentNode = None, self.head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        return previousNode
    
linkedlist = LinkedList()
input_list = [1, 2, 3, 4]

for e in input_list:
    linkedlist.append(e)

node = linkedlist.reverse()

while node:
    print(node.value)
    node = node.next
