class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = float('inf')
        while l <= r:
            speed = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            if hours <= h:
                min_k = min(min_k, speed)
                r = speed - 1
            else:
                l = speed + 1
        return min_k