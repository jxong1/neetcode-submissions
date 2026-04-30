class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        vector<vector<int>> counts(nums.size() + 1);
        vector<int> output;
        for (auto num: nums) {
            seen[num]++;
        }

        for (auto kv: seen) {
            int key = kv.first;
            int value = kv.second;

            counts[value].push_back(key);
        }

        for (int i = counts.size() - 1; i >= 0; i--) {
            for (auto num: counts[i]) {
                output.push_back(num);
                if (output.size() == k) {
                    return output;
                }
            }
        }
    }
};
