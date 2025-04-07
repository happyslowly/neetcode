# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  # type: ignore

        index_map = {n: i for i, n in enumerate(inorder)}
        queue = deque(preorder)

        def build(l, r) -> Optional[TreeNode]:  # type: ignore
            if l > r:
                return None
            val = queue.popleft()
            root = TreeNode(val)  # type: ignore
            m = index_map[val]
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(preorder) - 1)


# @leet end

