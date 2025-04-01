# @leet start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                a, b = i, nums[i] - 1
                nums[a], nums[b] = nums[b], nums[a]
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


# @leet end
