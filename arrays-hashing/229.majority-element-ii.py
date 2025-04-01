# @leet start
from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1

        results = []

        if count1 > len(nums) // 3:
            results.append(candidate1)
        if count2 > len(nums) // 3:
            results.append(candidate2)

        return results


# @leet end
