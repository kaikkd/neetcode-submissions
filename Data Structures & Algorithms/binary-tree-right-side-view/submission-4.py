# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        depth = 0

        def dfs(root, dp):
            if not root:
                return None
            
            nonlocal res, depth

            if dp == depth:
                res.append(root.val)
                depth += 1
            
            right = dfs(root.right, dp + 1)
            left = dfs(root.left, dp + 1)
        
        dfs(root, 0)
        return res