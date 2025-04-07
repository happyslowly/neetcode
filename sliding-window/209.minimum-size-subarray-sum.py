# @leet start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        curr_sum = 0
        min_length = len(nums) + 1
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_length = min(min_length, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        return min_length if min_length <= len(nums) else 0


# @leet end

