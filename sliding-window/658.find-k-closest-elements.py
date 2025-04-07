# @leet start

from collections import deque


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        queue = deque()
        l = 0
        for r in range(len(arr)):
            if len(queue) == k:
                if abs(arr[l] - x) > abs(arr[r] - x):
                    l += 1
                    queue.popleft()
            if len(queue) < k:
                queue.append(arr[r])
        return list(queue)


# @leet end

