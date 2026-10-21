class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        safeq = deque()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        def bfs(q):
            while q:
                x, y = q.popleft()
                for a, b in directions:
                    x2, y2 = x + a, y + b
                    if (x2, y2) not in safe and 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == "O":
                        safe.add((x2, y2))
                        q.append((x2, y2))

        for i in range(m):
            if board[i][0] == "O":
                safe.add((i, 0))
                safeq.append((i, 0))

            if board[i][n - 1] == "O":
                safe.add((i, n - 1))
                safeq.append((i, n - 1))
        
        for i in range(n):
            if board[0][i] == "O":
                safe.add((0, i))
                safeq.append((0, i))
            
            if board[m - 1][i] == "O":
                safe.add((m - 1, i))
                safeq.append((m - 1, i))

        bfs(safeq)
        for i in range(m):
            for j in range(n):
                if (i, j) not in safe:
                    board[i][j] = "X"