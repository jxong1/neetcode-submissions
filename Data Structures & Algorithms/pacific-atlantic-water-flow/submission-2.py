class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        pq = deque()
        aq = deque()

        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            pacific.add((i, 0))
            pq.append((i, 0))
            atlantic.add((i, n - 1))
            aq.append((i, n - 1))

        for i in range(n):
            pacific.add((0, i))
            pq.append((0, i))
            atlantic.add((m - 1, i))
            aq.append((m - 1, i))

        def bfs(q, tiles):
            visited = set()
            while q:
                x, y = q.popleft()
                for a, b in directions:
                    x2, y2 = x + a, y + b
                    if (x2, y2) not in visited and 0 <= x2 < m and 0 <= y2 < n and heights[x2][y2] >= heights[x][y]:
                        visited.add((x2, y2))
                        tiles.add((x2, y2))
                        q.append((x2, y2))
        
        bfs(pq, pacific)
        bfs(aq, atlantic)
        return [(a, b) for a in range(m) for b in range(n) if (a,b) in pacific and (a,b) in atlantic]