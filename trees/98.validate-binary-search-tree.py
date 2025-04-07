# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  # type: ignore
        def dfs(root: Optional[TreeNode]):  # type: ignore
            if not root:
                return True, math.inf, -math.inf
            is_left_bst, left_min, left_max = dfs(root.left)
            is_right_bst, right_min, right_max = dfs(root.right)
            return (
                is_left_bst and is_right_bst and left_max < root.val < right_min,
                min(left_min, root.val),
                max(right_max, root.val),
            )

        return dfs(root)[0]


# @leet end

