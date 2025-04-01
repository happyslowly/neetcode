# @leet start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        results = []
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return "".join(results)
            results.append(c)

        return "".join(results)


# @leet end

