# @leet start
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in counter.items():
            buckets[c].append(n)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[i][:k])
            k -= len(buckets[i])
            if k <= 0:
                break
        return result


# @leet end
