# @leet start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        max_length = 0
        for n in s:
            if n - 1 not in s:
                length = 1
                while (n + length) in s:
                    length += 1
                max_length = max(max_length, length)
        return max_length


# @leet end
