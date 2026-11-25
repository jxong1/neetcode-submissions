class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                ans += 1
        return ans