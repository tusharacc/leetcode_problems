
"""
Given a binary tree, return all paths from root to leaf.

For your reference:

"""

import random

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def helper(node,slate=[],result=[]):
    if (not node.left) or (not node.right) :
        slate.append(node.value)
        return result.append(slate[:])
    
    slate.append(node.value)
    helper(node.left,slate,result)
    slate.pop()
    helper(node.right,slate,result)
    print (slate, result)

def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    return helper(root)

if __name__ == '__main__':
    counter = 0
    root = BinaryTreeNode(1)
    two = BinaryTreeNode(2)
    three = BinaryTreeNode(3)
    four = BinaryTreeNode(4)
    five = BinaryTreeNode(5)
    six = BinaryTreeNode(6)
    seven = BinaryTreeNode(7)
    root.left = two
    root.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven

    all_paths_of_a_binary_tree(root)
