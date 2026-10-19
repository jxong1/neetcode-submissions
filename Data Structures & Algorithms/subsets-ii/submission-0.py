class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def bt(start = 0, arr = []):
            ans.append(arr.copy())
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                bt(i + 1, arr)
                arr.pop()

        bt()
        return ans