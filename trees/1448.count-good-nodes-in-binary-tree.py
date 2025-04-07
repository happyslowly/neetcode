# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def goodNodes(self, root: TreeNode) -> int:  # type: ignore
        def dfs(root: TreeNode, curr_max) -> int:  # type: ignore
            if not root:
                return 0
            return (
                (1 if curr_max <= root.val else 0)
                + dfs(root.left, max(curr_max, root.val))
                + dfs(root.right, max(curr_max, root.val))
            )

        return dfs(root, -math.inf)


# @leet end

