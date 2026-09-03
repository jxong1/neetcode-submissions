class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * n
        for i in range(1, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]