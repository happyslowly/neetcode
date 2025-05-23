# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # type: ignore
        stack = []
        result = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result.append(node.val)
        result.reverse()
        return result


# @leet end

