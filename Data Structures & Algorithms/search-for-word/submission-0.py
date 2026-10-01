class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bt(i, j, idx):
            if idx == len(word):
                return True
                
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False

            if word[idx] == board[i][j]:

                temp = board[i][j]
                board[i][j] = ''

                if bt(i-1, j, idx+1) or bt(i+1, j, idx+1) or bt(i, j-1, idx+1) or bt(i, j+1, idx+1):
                    return True
                
                board[i][j] = temp
                return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and bt(i, j, 0):
                    return True
        return False