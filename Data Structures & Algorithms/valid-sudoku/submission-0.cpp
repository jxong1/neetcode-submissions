class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {
            set<int> count;
            for (int j = 0; j < board.size(); j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int num = board[i][j];
                if (count.find(board[i][j]) != count.end()) {
                    return false;
                }
                count.insert(board[i][j]);
            }
        }

        for (int i = 0; i < board.size(); i++) {
            set<int> count;
            for (int j = 0; j < board.size(); j++) {
                if (board[j][i] == '.') {
                    continue;
                }
                int num = board[j][i];
                if (count.find(board[j][i]) != count.end()) {
                    return false;
                }
                count.insert(board[j][i]);
            }
        }

        for (int i = 0; i < board.size(); i += 3) {
            for (int j = 0; j < board.size(); j += 3) {
                unordered_map<int, int> freq;
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        if (board[i + k][j + l] != '.') {
                            freq[board[i + k][j + l]]++;
                        }
                    }
                }
                for (auto [key, value]: freq) {
                    if (value > 1) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
