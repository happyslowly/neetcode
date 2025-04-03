# @leet start
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        total = 0
        while l <= r:
            if left_max < right_max:
                total += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
                l += 1
            else:
                total += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
                r -= 1
        return total


# @leet end
