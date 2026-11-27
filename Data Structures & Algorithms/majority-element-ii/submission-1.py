class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums) // 3
        prev = None
        count = 0
        ans = []
        for i in range(len(nums)):
            if prev is not None and nums[i] == prev:
                count += 1
            else:
                count = 1
            prev = nums[i]
            if count > n and (not ans or nums[i] != ans[-1]):
                ans.append(nums[i])
        return ans