# @leet start
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        result = []
        for s in strs:
            result.append(str(len(s)) + "@" + s)
        return "".join(result)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        i = 0
        results = []
        while i < len(s):
            j = s.index("@", i)
            length = int(s[i:j])
            results.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return results


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @leet end

