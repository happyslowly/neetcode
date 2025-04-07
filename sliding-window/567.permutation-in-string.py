# @leet start
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen1 = defaultdict(int)
        for c1 in s1:
            seen1[c1] += 1

        seen2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            seen2[s2[r]] += 1
            if r - l + 1 >= len(s1):
                if seen1 == seen2:
                    return True
                seen2[s2[l]] -= 1
                if seen2[s2[l]] == 0:
                    del seen2[s2[l]]
                l += 1
        return False


# @leet end

