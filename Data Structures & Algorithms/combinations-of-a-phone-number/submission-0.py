class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans = []
        strArr = []
        mapping = [['a','b','c'], ['d','e','f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p','q','r','s'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        def bt(start):
            if start == len(digits):
                ans.append("".join(strArr))
                return
            dig = digits[start]
            letters = mapping[ord(dig)- ord('2')]

            for l in letters:
                strArr.append(l)
                bt(start + 1)
                strArr.pop()
        
        bt(0)
        return ans