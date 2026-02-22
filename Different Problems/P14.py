class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        word = strs[0]
        # word = 'flower'
        for i in range(len(word), 0, -1):
            prefix = word[:i]
            count = 0
            for j in range(1, len(strs)):
                if strs[j].startswith(prefix):
                    count += 1
                if count == (len(strs) - 1):
                    return prefix
        return ""


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
