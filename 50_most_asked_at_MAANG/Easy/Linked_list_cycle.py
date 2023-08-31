'''
Linked List Cycle 

Given head, the head of a linked list, determine if the linked list has a cycle in it. 

there is a cycle in a linked list if there is some node in the list that can be reached again by continously following the next pointer. Internally, 
pos is used to denote the index of the node that tails next pointer is connected to. Note that pos is not passed as a paramter. 

Return true if there is a cycle in the linked list, otherwise return false. 

'''

# O(n) time | O(1) space

class LinkedListL:
    def __init__(self, value):
        self.value = value
        self.next = None


def findCycle(head):
    first = head.next
    second = head.next.next
    
    while second and second.next:
        first = first.next
        second = second.next.next  
        if first == second:
            return True
    
    return False