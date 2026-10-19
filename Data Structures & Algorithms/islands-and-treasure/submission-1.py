class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        def bfs(q):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                x, y, dist = q.popleft()
                if dist > grid[x][y]:
                    continue
                grid[x][y] = min(grid[x][y], dist)
                for a, b in directions:
                    if x + a >= 0 and x + a < len(grid) and y + b >= 0 and y + b < len(grid[0]):
                        if grid[x + a][y + b] == 2147483647:
                            grid[x + a][y + b] = dist + 1
                            q.append([x + a, y + b, dist + 1])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    q.append([x, y, 0])
        
        bfs(q)