# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  # type: ignore
        def dfs(root: Optional[TreeNode]):  # type: ignore
            if not root:
                return 0, True
            left_height, is_left_balanced = dfs(root.left)
            right_height, is_right_balanced = dfs(root.right)
            height = max(left_height, right_height) + 1
            is_balanced = (
                abs(left_height - right_height) <= 1
                and is_left_balanced
                and is_right_balanced
            )
            return height, is_balanced

        return dfs(root)[1]


# @leet end

