'''
Given a tree, find its height: number of edges in the longest path from the root to any node.
'''

"""
For your reference:
"""

from queue import Queue

q = Queue()

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
def find_height(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    q.put(root)
    temp = []
    height = 0
    while True:
        while not q.empty():
            node = q.get()
            
            for item in node.children:
                temp.append(item)
        height += 1
        if not temp:
            break
        else:
            while temp:
                q.put(temp.pop())

    return height
if __name__ == '__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    five = TreeNode(5)
    four = TreeNode(4)
    one.children.append(two)
    one.children.append(three)
    one.children.append(five)
    five.children.append(four)
    print (find_height(one))