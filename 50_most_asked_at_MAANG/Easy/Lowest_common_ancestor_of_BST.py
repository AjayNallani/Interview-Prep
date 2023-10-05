'''
Given a binary search tree(BST), find the lowest common ancestor node of two given nodes in the BST

Accroding to the definition of LCA : the lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both 
p and q as descendants (where we allow a node to be a descendent of itself)

'''

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
    
def lowestCommonAncestor(root:'TreeNode', p:'TreeNode', q:'TreeNode') -> 'TreeNode':

    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val  and q.val < curr.val:
            curr = curr.left
        else:
            return curr