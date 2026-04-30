class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, vector<int>> sequences;
        sort(nums.begin(), nums.end());

        for (auto num: nums) {
            for (auto [key, arr]: sequences) {
                if (arr[arr.size() - 1] == num - 1) {
                    sequences[key].push_back(num);
                    continue;
                }
            }
            if (sequences.find(num) == sequences.end()) {
                sequences[num].push_back(num); // New sequence
            }
        }

        int largest = 0;
        for (auto [key, arr]: sequences) {
            if (arr.size() > largest) { largest = arr.size(); }
        }
        return largest;
    }
};
