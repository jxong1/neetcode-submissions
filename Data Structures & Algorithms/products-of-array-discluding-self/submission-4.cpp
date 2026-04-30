class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int total = 1;
        int zeros = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                zeros++;
                continue;
            }
            total = total * nums[i];
        }

        vector<int> output;
        if (zeros > 1) {
            return vector<int>(nums.size(), 0);
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                output.push_back(total);
            }
            else if (zeros > 0) {
                output.push_back(0);   
            }
            else {
                output.push_back(total / nums[i]);
            }
        }
        return output;
    }
};
