# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:  # type: ignore
        def dfs(root: Optional[TreeNode]) -> tuple[int, int]:  # type: ignore
            if not root:
                return 0, 0
            max_left_include, max_left_exclude = dfs(root.left)
            max_right_include, max_right_exclude = dfs(root.right)
            return (
                root.val + max_left_exclude + max_right_exclude,
                max(max_left_include, max_left_exclude)
                + max(max_right_include, max_right_exclude),
            )

        return max(dfs(root))


# @leet end

