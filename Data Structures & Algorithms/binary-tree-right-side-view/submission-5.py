# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur_dp = 0

        def dfs(root, depth):
            if not root:
                return 0
            
            nonlocal res, cur_dp
            if depth == cur_dp:
                cur_dp += 1
                res.append(root.val)
            right = dfs(root.right, depth + 1)
            left = dfs(root.left, depth + 1)
        
        dfs(root, 0)
        return res