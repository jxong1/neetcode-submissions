class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in (0, 1):
                left, right = i, i + j
                while left > -1 and right < len(s):
                    if s[left] == s[right]:
                        res += 1
                        left -= 1
                        right += 1
                    else:
                        break
        return res