class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        subStrs = []

        def bt(start):
            if start == len(s):
                ans.append(subStrs.copy())
            for i in range(start, len(s)):
                subStr = s[start: i + 1]
                if subStr == subStr[::-1]:
                    subStrs.append(subStr)
                    bt(i + 1)
                    subStrs.pop()
        bt(0)
        return ans