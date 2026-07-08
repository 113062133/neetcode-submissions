# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        n = len(inorder)
        for i in range(n):
            m[inorder[i]] = i
        
        self.pre_idx = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root_idx = m[root_val]

            root = TreeNode(root_val)
            root.left = dfs(left, root_idx - 1)
            root.right = dfs(root_idx + 1, right)
            return root
        
        return dfs(0, n - 1)

