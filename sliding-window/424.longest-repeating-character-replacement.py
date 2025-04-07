# @leet start
from collections import defaultdict


# BAA
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)

        l = 0
        max_length = 0
        for r in range(len(s)):
            seen[s[r]] += 1

            total = r - l + 1
            while total - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
                total = r - l + 1
            max_length = max(max_length, r - l + 1)
        return max_length


# @leet end

