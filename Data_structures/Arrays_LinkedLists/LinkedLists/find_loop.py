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

    def find_loop(self):
        if self.head is None:
            return False

        slow = linkedlist.head
        fast = linkedlist.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
    
linkedlist = LinkedList()
input_list = [1, 2, 3, 4]

for e in input_list:
    linkedlist.append(e)

node = linkedlist.head
while node:
    print(node.value)
    node = node.next

# list_with_loop = linkedlist
# loop_start = list_with_loop.head.next

# node = list_with_loop.head
# while node.next:
#     node = node.next
# node.next = loop_start

print(linkedlist.find_loop())