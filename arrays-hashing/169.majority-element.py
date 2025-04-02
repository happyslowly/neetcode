# @leet start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate, count = None, 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        assert candidate is not None
        return candidate


# @leet end
