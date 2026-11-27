class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return True if (s[l + 1: r + 1] == s[r: l: -1] or s[l: r] == s[r - 1: l - 1 if l > 0 else None: -1]) else False
            l += 1
            r -= 1
        return True
