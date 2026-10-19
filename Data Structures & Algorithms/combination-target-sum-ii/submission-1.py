class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        def bt(start, arr, total):
            if total == target:
                ans.append(arr.copy())
            elif total > target:
                return

            for i in range(start, len(candidates)):
                if i != start and candidates[i-1] == candidates[i]:
                    continue
                arr.append(candidates[i])
                bt(i + 1, arr, total + candidates[i])
                arr.pop()
        bt(0, [], 0)
        return ans