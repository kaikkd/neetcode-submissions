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
            nonlocal res

            if not root:
                return 0

            left_dp = dfs(root.left)
            right_dp = dfs(root.right)
            res = max(res, left_dp + right_dp)

            return 1 + max(left_dp, right_dp)
        
        dfs(root)

        return res