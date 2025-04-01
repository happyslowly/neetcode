# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        n = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            prefix[i] *= n
            n *= nums[i]
        return prefix


# @leet end

