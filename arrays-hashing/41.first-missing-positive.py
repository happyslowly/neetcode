# @leet start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if 0 <= correct_index < len(nums) and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1


# @leet end
