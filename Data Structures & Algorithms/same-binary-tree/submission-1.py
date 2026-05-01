# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_val, q_val):
            if not p_val and not q_val:
                return True
            
            if p_val and q_val and p_val.val == q_val.val:
                return dfs(p_val.left, q_val.left) and dfs(p_val.right, q_val.right)
            
            else:
                return False
            
        return dfs(p, q)