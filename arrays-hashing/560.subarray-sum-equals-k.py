# @leet start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        count = 0
        for n in nums:
            prefix += n
            if prefix - k in d:
                count += d[prefix - k]
            d[prefix] += 1
        return count


# @leet end

