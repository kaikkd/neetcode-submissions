# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, l_min, r_max):
            if not node:
                return True
            
            if l_min < node.val < r_max:
                return dfs(node.left, l_min, min(node.val, r_max)) and dfs(node.right, max(node.val, l_min), r_max)
            else:
                return False
        
        return dfs(root, -float('inf'), float('inf'))