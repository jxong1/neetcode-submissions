class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        ans = []
        def bfs(x, y):
            if x == 0 or y == 0:
                pacific.add((x, y))
            if x == len(heights) -1 or y == len(heights[0]) - 1:
                atlantic.add((x, y))

            if (x, y) in pacific and (x, y) in atlantic:
                return (x, y) in pacific, (x, y) in atlantic
            
            for a, b in directions:
                x2, y2 = x + a, y + b
                if 0 <= x2 < len(heights) and 0 <= y2 < len(heights[0]) and heights[x2][y2] <= heights[x][y]:
                    if (x2, y2) in visited:
                        if (x2, y2) in pacific:
                            pacific.add((x, y))
                        if (x2, y2) in atlantic:
                            atlantic.add((x, y))
                    else:
                        visited.add((x2, y2))
                        p, a = bfs(x2, y2)
                        if p:
                            pacific.add((x, y))
                        if a:
                            atlantic.add((x, y))
            return (x, y) in pacific, (x, y) in atlantic

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                bfs(i, j)
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        return ans