# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {inorder[i]: i for i in range(len(inorder))}

        def dfs(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e:
                return None
            
            root_val = preorder[pre_s]
            root_idx = indexMap[root_val]
            root = TreeNode(root_val)
            left = root_idx - in_s

            root.left = dfs(pre_s + 1, pre_s + left, in_s, root_idx - 1)
            root.right = dfs(pre_s + left + 1, pre_e, root_idx + 1, in_e)

            return root
            
        n = len(preorder)
        return dfs(0, n - 1, 0, n - 1)


