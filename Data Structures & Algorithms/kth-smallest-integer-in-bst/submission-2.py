# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        depth = 0
        res = root.val
        def dfs(node):
            if not node:
                return 
            
            nonlocal res, cnt
            dfs(node.left)

            if cnt == 0:
                return
            
            cnt -= 1
            if cnt == 0:
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res
                