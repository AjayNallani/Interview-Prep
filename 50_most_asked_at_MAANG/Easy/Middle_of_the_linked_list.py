'''
Given the head of a singly linked list, return the middle node of the linked list 

if there are two middle nodes, return the second middle node 

'''

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
        
        # iterate until the end of the linkedlist is reached
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)

        return

numList = [1, 2, 3, 4, 5]
linkedlist = LinkedList()

for e in numList:
    linkedlist.append(e)

node = linkedlist.head
count = 0
while node:
    count += 1
    print(node.value)
    node = node.next

print(count)

# iterate two pointers traversing both one at normal speed and the other at twice the speed. 
first = linkedlist.head
second = linkedlist.head

while second and second.next:
    first = first.next
    second = second.next.next
print(first.value)

