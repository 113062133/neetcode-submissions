# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ans = -1

        def dfs(node):
            if not node or self.ans >= 0:
                return

            dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.ans = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.ans