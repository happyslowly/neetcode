# @leet start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] == val:
                continue
            nums[i] = nums[j]
            i += 1
        return i


# @leet end

