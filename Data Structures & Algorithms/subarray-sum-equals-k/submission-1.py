class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        preSums = {0: 1}
        ans = 0
        for i in range(len(nums)):
            pre += nums[i]
            ans += preSums.get(pre - k, 0)
            preSums[pre] = preSums.get(pre, 0) + 1
        return ans