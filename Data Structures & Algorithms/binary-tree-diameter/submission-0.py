# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # find max length in left and right and add them together
        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            res = max(res, l + r)

            return 1 + max(l, r)  
        
        res = 0
        dfs(root)
        return res