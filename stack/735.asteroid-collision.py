# @leet start
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                x = stack.pop()
                y = stack.pop()
                if abs(x) > abs(y):
                    stack.append(x)
                elif abs(x) < abs(y):
                    stack.append(y)
        return stack


# @leet end

