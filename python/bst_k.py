
'''
Given a binary search tree (BST) and an integer k, find k-th smallest element.
'''
"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isLeaf(node):
    if node.left == None and node.right == None:
        return True
    return False

def helper(node,k):
    if isLeaf(node):
        k=k-1
def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.

    return 0
