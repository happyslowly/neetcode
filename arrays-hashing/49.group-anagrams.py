# @leet start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = defaultdict(list)
        for s in strs:
            array = [0] * 26
            for c in s:
                array[ord(c) - ord("a")] += 1
            results[tuple(array)].append(s)
        return list(results.values())


# @leet end

