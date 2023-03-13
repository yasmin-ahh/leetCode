# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True 
        def checkValid(right, left): 
            if not right and not left: 
                return True 
            if not right or not left:
                return False
            if right.val == left.val: 
                return checkValid(left.left, right.right) and checkValid(left.right, right.left)
            return False
        return checkValid(root.right, root.left)
