# @leet start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, -1, len(nums)
        while i < r:
            if nums[i] == 0:
                l += 1
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1


# @leet end

