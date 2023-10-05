'''
Given the root of a binary tree, return its maximum depth 

A binary tree maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

'''

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def maxDepth(root: Node) -> int:
    if not root:
        return 0 

    return 1 + max(maxDepth(root.left), maxDepth(root.right)) 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(maxDepth(root))