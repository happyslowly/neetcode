# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:  # type: ignore
        if not root:
            return False
        return (
            self._is_same_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def _is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  # type: ignore
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        return (
            p.val == q.val
            and self._is_same_tree(p.left, q.left)
            and self._is_same_tree(p.right, q.right)
        )


# @leet end

