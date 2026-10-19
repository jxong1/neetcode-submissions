class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(arr, tracker):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                
            for num in nums:
                if num not in tracker:
                    arr.append(num)
                    tracker.add(num)
                    bt(arr, tracker)
                    arr.pop()
                    tracker.remove(num)

        bt([], set())
        return ans