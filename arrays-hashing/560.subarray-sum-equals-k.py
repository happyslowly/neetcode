# @leet start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        curr_sum = 0
        count = 0

        for n in nums:
            curr_sum += n
            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1
        return count


# @leet end
