# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0
        indexes = {val : idx for idx, val in enumerate(inorder)}

        def bfs(l, r):
            if l > r:
                return None
            
            nonlocal pre_index
            
            node_val = preorder[pre_index]
            root = TreeNode(node_val)
            pre_index += 1
            mid = indexes[node_val]

            root.left = bfs(l, mid - 1)
            root.right = bfs(mid + 1, r)

            return root
        return bfs(0, len(inorder) - 1)