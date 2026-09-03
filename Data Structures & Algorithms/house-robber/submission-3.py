class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return max(dp)