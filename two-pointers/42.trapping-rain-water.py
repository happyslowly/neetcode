# @leet start
class Solution:
    def trap(self, height: list[int]) -> int:
        max_right = [height[-1]] * len(height)
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        total = 0
        max_left = height[0]
        for i in range(1, len(height)):
            total += max(0, min(max_left, max_right[i]) - height[i])
            max_left = max(max_left, height[i])
        return total


# @leet end

