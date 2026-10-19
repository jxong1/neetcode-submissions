class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def bt(start = 0, arr = []):
            ans.append(arr.copy())
            for i in range(start, len(nums)):
                arr.append(nums[i])
                bt(i + 1, arr)
                arr.pop()

        bt()
        return ans