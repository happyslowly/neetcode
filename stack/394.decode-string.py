# @leet start
class Solution:
    def decodeString(self, s: str) -> str:
        curr_num, curr_str = 0, ""
        stack = []
        for c in s:
            if c.isdigit():
                curr_num = 10 * curr_num + int(c)
            elif c.isalpha():
                curr_str += c
            elif c == "[":
                stack.append((curr_num, curr_str))
                curr_num, curr_str = 0, ""
            else:
                last_num, last_str = stack.pop()
                curr_str = last_str + last_num * curr_str
        return curr_str


# @leet end
