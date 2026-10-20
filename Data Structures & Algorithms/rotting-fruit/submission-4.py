class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        time = 0
        fresh = 0

        def bfs():
            nonlocal fresh, time
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q and fresh > 0:
                for i in range(len(q)):
                    x, y = q.popleft()   
                    for a, b in directions:
                        x2, y2 = x + a, y + b
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 1:
                            grid[x2][y2] = 2
                            fresh -= 1
                            q.append((x2, y2))
                time += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if q:
            bfs()
        return time if fresh == 0 else -1