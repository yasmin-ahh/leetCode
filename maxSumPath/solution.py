# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxCount = float('-inf') 
        def dfsFunction(node): 
            nonlocal maxCount
            if not node: 
                return 0 
            
            leftNode = max(dfsFunction(node.left), 0) 
            rightNode = max(dfsFunction(node.right), 0) 

            maxCount = max(maxCount, node.val + leftNode + rightNode)

            return max(leftNode, rightNode) + node.val
        dfsFunction(root)
        return maxCount
