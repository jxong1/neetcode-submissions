class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = count = 0
        for num in nums:
            if count == 0 or num == ans:
                ans = num
                count += 1
            else:
                count -= 1
        return ans