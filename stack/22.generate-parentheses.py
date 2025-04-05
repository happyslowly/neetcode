# @leet start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs(open_count, close_count, path):
            if len(path) == 2 * n:
                result.append(path)
                return
            if open_count < n:
                dfs(open_count + 1, close_count, path + "(")
            if close_count < open:
                dfs(open, close_count + 1, path + ")")

        dfs(0, 0, "")
        return result


# @leet end
