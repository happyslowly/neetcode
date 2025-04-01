# @leet start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        m = 0
        for n in s:
            if n - 1 not in s:
                length = 1
                while (n + length) in s:
                    length += 1
                m = max(m, length)
        return m


# @leet end

