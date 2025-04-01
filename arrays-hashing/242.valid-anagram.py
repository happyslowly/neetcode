# @leet start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            if d[c] == 0:
                return False
            d[c] -= 1
        return True


# @leet end

