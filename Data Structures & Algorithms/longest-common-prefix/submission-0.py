class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(len(ans)):
            for s in strs:
                if i == len(s) or s[i] != ans[i]:
                    return ans[:i]
        return ans