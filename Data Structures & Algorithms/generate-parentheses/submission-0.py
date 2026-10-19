class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        ans = []
        def bt(s, bal):
            if len(s) == n * 2:
                if bal == 0:
                    ans.append("".join(s))
                return
            
            s.append("(")
            bt(s, bal + 1)
            s.pop()
            
            if bal > 0:
                s.append(")")
                bt(s, bal - 1)
                s.pop()
            

        bt(["("], 1)
        return ans