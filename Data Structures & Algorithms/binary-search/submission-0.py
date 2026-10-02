class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif target < num:
                r = mid - 1
            else:
                l = mid + 1
        return -1