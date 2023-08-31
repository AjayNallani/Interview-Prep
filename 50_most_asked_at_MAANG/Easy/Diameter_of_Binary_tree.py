'''
Diameter of binary tree 
Given the root of a binary tree, return the length of the diameter of the tree 

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes. the length of the path 
is the number of edges between the paths first node and its last node 

Each BinaryTree node has an integer value, a left child node and a right child node. Children nodes can either be BinaryTree nodes themselves 
or None/null

'''

class BinaryTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

def BinaryTreeDiameter(tree):

    return getTreeInfo(tree).diameter

def getTreeInfo(tree):

    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiamter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiamter, currentHeight)


