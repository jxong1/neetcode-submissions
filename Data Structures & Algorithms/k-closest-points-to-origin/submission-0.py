class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        hsh = {}
        for point in points:
            dist = point[0]** 2 + point[1]**2
            hsh[dist] = hsh.get(dist, []) + [point]
        dists = list(hsh.keys())
        heapq.heapify(dists)
        i = 0
        while i < k:
            dist = heapq.heappop(dists)
            for point in hsh[dist]:
                res.append(point)
                i += 1
                if i == k:
                    break
        return res