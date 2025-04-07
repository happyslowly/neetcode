# @leet start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":  # type: ignore

        def dfs(x, y, n):
            is_leaf = True
            val = grid[x][y]

            for i in range(x, x + n):
                for j in range(y, y + n):
                    if grid[i][j] != val:
                        is_leaf = False
                        break
                if not is_leaf:
                    break
            if is_leaf:
                return Node(val, True)  # type: ignore
            else:
                root = Node(1, False)  # type: ignore
                n //= 2
                root.topLeft = dfs(x, y, n)
                root.topRight = dfs(x, y + n, n)
                root.bottomLeft = dfs(x + n, y, n)
                root.bottomRight = dfs(x + n, y + n, n)
                return root

        return dfs(0, 0, len(grid))


# @leet end

