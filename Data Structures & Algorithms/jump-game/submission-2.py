class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        target = len(nums)
        for i in range(target):
            if i > furthest:
                return False
            furthest = max(furthest, nums[i] + i)
            if furthest >= target:
                return True
        return True
            