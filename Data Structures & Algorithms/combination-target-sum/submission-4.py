class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def bt(comb, t, i):
            if t == 0:
                res.append(comb.copy())
            if t > 0:
                for j in range(i, len(nums)):
                    num = nums[j]
                    comb.append(num)
                    bt(comb, t-num, j)
                    comb.pop()

        res = []
        bt([], target, 0)
        return res