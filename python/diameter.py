'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

from typing import Optional

max_height = 0
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(node):
    if not node:
        return 0
    global max_height

    LH = helper(node.left)
    RH = helper(node.right)

    max_height = max(LH+RH,max_height)

    return max(LH,RH)+1

def diameterOfBinaryTree( root: Optional[TreeNode]) -> int:
    helper(root)
    return max_height

if __name__ == '__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    print(diameterOfBinaryTree(one))