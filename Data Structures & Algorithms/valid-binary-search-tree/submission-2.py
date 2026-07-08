# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, left, right):
            if not node:
                return True
            node_valid = left < node.val and node.val < right and (not node.left or node.left.val < node.val) and (not node.right or node.val < node.right.val)
            left_valid = dfs(node.left, left, node.val)
            right_valid = dfs(node.right, node.val, right)
            return node_valid and left_valid and right_valid

        return dfs(root, -float("inf"), float("inf"))