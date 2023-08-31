'''
Given a binary tree, determine if it is height balanced. 

You're given a root node of the binary tree. Write a function that returns true if this binary tree is height balanced and false if it isn't

A binary tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of 
its right subtree is at most 1 

Each BinaryTree node has an integer value, a left child node and a right child node. Children nodes can either be BinaryTree nodes 
themselves or None/null.

'''

# O(n) time | O(h) space - where n is the number of nodes and height is the height 

class Node:
    def __init__(self, value, left=None, right= None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced: bool, height: int):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree) -> bool:
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    
    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = (leftSubTreeInfo.isBalanced and 
                  rightSubTreeInfo.isBalanced and 
                  abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1)

    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1

    return TreeInfo(isBalanced, height)



BT = {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": None, "right": "6", "value": 3},
      {"id": "4", "left": None, "right": None, "value": 4},
      {"id": "5", "left": "7", "right": "8", "value": 5},
      {"id": "6", "left": None, "right": None, "value": 6},
      {"id": "7", "left": None, "right": None, "value": 7},
      {"id": "8", "left": None, "right": None, "value": 8}
    ],
    "root": "1"
    }

def createBinaryTree(BT):
    root = BT['root']

    for id in len((BT['nodes'])):

        if id != root:
            value = BT['nodes'][id]['value']
            left = BT['nodes'][id]['left']
            right = BT['nodes'][id]['right']

            node = Node(value, left, right)

    return root
