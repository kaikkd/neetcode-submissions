# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_v, max_v = -float('inf'), float('inf')

        def dfs(node, l_min, r_max):
            if not node:
                return True
            
            if not l_min < node.val < r_max:
                return False
            
            return (dfs(node.left, l_min, min(r_max, node.val)) and dfs(node.right, max(l_min, node.val), r_max))
        
        return dfs(root, min_v, max_v)