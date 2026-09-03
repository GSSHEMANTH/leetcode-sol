# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        def isMirror(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            if left_node is None or right_node is None:
                return False
            return (left_node.val == right_node.val and 
                    isMirror(left_node.left, right_node.right) and 
                    isMirror(left_node.right, right_node.left))
                    
        return isMirror(root.left, root.right)

        
        