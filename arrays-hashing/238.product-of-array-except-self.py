# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        prefix = 1
        for i, n in enumerate(nums):
            result[i] = prefix
            prefix = result[i] * n
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result


# @leet end
