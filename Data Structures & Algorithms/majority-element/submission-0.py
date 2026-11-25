class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        ans = 0
        maj = None
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > ans:
                ans = counts[num]
                maj = num
        return maj