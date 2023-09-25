class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    def traveseLL(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
    
input_list = [1, 2, 3, 4, 5, 6]

linked_list = SinglyLinkedList()

for e in input_list:
    linked_list.append(e)

linked_list.traveseLL()
