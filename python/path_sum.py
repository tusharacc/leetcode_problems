'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(node: TreeNode, targetSum):
    if node:
        if node.left == None and node.right == None:
            if targetSum - node.val == 0:
                return True
            return False 
        
        if helper(node.left,targetSum - node.val):
            return True
        return helper(node.right, targetSum - node.val)
    return False
def hasPathSum( root: Optional[TreeNode], targetSum: int) -> bool:
        return helper(root,targetSum)

if __name__ == '__main__':
    # five = TreeNode(5)
    # four = TreeNode(4)
    # eight = TreeNode(8)
    # eleven = TreeNode(11)
    # seven = TreeNode(7)
    # two = TreeNode(2)
    # thirteen = TreeNode(13)
    # four = TreeNode(4)
    # one = TreeNode(1)

    # five.left = four
    # five.right = eight

    # four.left = eleven

    # eleven.left = seven
    # eleven.right = two
    
    # eight.left = thirteen
    # eight.right = four

    # four.right = one

    #test case 2
    one = TreeNode(1)
    two = TreeNode(2)
    one.right = two
    print(hasPathSum(one,0))