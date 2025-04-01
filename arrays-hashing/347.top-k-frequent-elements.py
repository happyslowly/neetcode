# @leet start
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = []
        for n, c in counter.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)

        results = []
        for c, n in heap:
            results.append(n)
        return results


# @leet end

