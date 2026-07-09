# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")

        def dfs(node):
            if node is None:
                return 0

            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            bothSum = leftSum + rightSum
            maxSum = max(leftSum, rightSum, bothSum) + node.val
            self.ans = max(self.ans, maxSum)
            return max(max(leftSum, rightSum) + node.val, 0)
        dfs(root)
        return self.ans