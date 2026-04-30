class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        int longest = 0;
        for (auto num: nums) {
            if (s.find(num - 1) != s.end()) { continue; }
            else {
                int curr_len = 1;
                int next_num = num + 1;

                while (s.find(next_num) != s.end()) {
                    curr_len++;
                    next_num++;
                }
                if (curr_len > longest) { longest = curr_len; }
            }
        }
        return longest;
    }
};
