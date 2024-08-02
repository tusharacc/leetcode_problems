'''
Given a binary tree, list the node values level by level from left to right.
'''

import queue

q = queue.Queue()
#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def helper(result: list):

    if q.empty():
        return

    temp: list = []
    while not q.empty():
        temp.append(q.get())
    
    for item in temp:
        if item.left:
            q.put(item.left)
        if item.right:
            q.put(item.right)

    result.append([item.value for item in temp])

    helper(result)

def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    result = []
    q.put(root)
    # Write your code here.
    helper(result)
    return result

if __name__ == '__main__':
    two = BinaryTreeNode(2)
    five = BinaryTreeNode(5)
    four = BinaryTreeNode(4)
    zero = BinaryTreeNode(0)
    one = BinaryTreeNode(1)
    three = BinaryTreeNode(3)
    six = BinaryTreeNode(6)
    
    two.left = five
    two.right = four

    five.left = zero
    five.right = one

    four.left = three
    four.right = six

    print(level_order_traversal(two))