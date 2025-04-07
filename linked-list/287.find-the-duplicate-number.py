# @leet start
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        n = len(nums)
        while fast < n and nums[fast] < n:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# @leet end

