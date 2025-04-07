# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # type: ignore
        stack = []
        p = root
        result = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                result.append(node.val)
                p = node.right
        return result


# @leet end

