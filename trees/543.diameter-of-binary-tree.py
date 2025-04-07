# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  # type: ignore
        def dfs(root: Optional[TreeNode]):  # type: ignore
            if not root:
                return 0, 0
            left_height, left_diameter = dfs(root.left)
            right_height, right_diameter = dfs(root.right)
            height = max(left_height, right_height) + 1
            diameter = max(left_height + right_height, left_diameter, right_diameter)
            return height, diameter

        return dfs(root)[1]


# @leet end

