# @leet start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        func_map = {
            "+": lambda b, a: a + b,
            "-": lambda b, a: a - b,
            "*": lambda b, a: a * b,
            "/": lambda b, a: int(a / b),
        }
        stack = []
        for c in tokens:
            if c in func_map:
                stack.append(func_map[c](stack.pop(), stack.pop()))
            else:
                stack.append(int(c))
        return stack.pop()


# @leet end

