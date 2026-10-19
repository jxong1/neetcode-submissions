class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        seen = set()
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in seen or grid[x][y] == "0":
                return
            seen.add((x, y))
            if grid[x][y] == "1":
                grid[x][y] = "0"
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for a, b in directions:
                dfs(x + a, y + b)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(x, y)
                    ans += 1
        return ans