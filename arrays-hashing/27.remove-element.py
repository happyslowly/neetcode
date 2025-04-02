# @leet start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            nums[slow] = nums[fast]
            slow += 1
        return slow


# @leet end
