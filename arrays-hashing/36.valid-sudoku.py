# @leet start
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        subs = defaultdict(set)
        for i in range(n):
            for j in range(n):
                c = board[i][j]
                if c == ".":
                    continue
                if c in rows[i] or c in cols[j] or c in subs[(i // 3, j // 3)]:
                    return False
                rows[i].add(c)
                cols[j].add(c)
                subs[(i // 3, j // 3)].add(c)

        return True


# @leet end

