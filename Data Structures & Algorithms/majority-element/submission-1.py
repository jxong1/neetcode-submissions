class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        prev = None
        count = 1
        maxcount = 1
        ans = None
        for num in nums:
            if num == prev:
                count += 1
            else:
                count = 1
                prev = num
            
            if count >= maxcount:
                maxcount = count
                ans = num
        return ans