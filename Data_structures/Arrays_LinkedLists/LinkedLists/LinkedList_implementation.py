

class Node:
    def __init__(self, value, next= None) -> None:
        self.value = value
        self.next = next

#creating a linked list using iteration 
def create_LL(input_list):
    
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head # when we have only one node, head and tail refer to the same node 
        else:
            tail.next = Node(value)
            tail = tail.next #update the trail 
    
    return head
    
def traverse_LL(node):
    current_node = node
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next
    return None

input_list = [1, 2, 3, 4, 5, 6]

head = create_LL(input_list)
traverse_LL(head)