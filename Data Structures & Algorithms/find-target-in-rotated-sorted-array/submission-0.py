class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: # Found
                return mid
            """
            Assuming nums = [1,2,3,4,5]
            If rotated 2 times -> [4,5,1,2,3]
            If rotated 3 times -> [3,4,5,1,2]

            If nums[mid] >= nums[left] -> nums[mid] in left side sorted portion
            Otherwise, nums[mid] in right side sorted portion
            """
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1




