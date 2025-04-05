# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        stack = []
        for c in s:
            if c in char_map:
                stack.append(c)
            elif stack and char_map[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return not stack


# @leet end

