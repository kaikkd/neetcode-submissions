# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            nonlocal res
            
            max_l = dfs(root.left)
            max_r = dfs(root.right)
            res = max(res, max_l + max_r)

            return 1 + max(max_l, max_r)
        
        dfs(root)
        return res