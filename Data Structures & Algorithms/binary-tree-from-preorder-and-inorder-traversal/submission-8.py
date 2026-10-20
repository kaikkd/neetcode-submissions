# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {num : index for index, num in enumerate(inorder)}
        pre_index = 0

        def dfs(l, r):
            if l > r:
                return None
            
            nonlocal pre_index
            val = preorder[pre_index]
            pre_index += 1
            root = TreeNode(val)
            mid = inorder_dict[val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)