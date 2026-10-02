class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        seen = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            elif i >= m or j >= n:
                return 0
            elif (i, j) in seen:
                return seen[(i, j)]
            if i > -1 and i < m and j > -1 and j < n:
                seen[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
                return seen[(i, j)]
        
        return dfs(0,0)