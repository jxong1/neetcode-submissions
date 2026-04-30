class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output(nums.size());
        int pre = 1;
        for (int i = 0; i < nums.size(); i++) {
            output[i] = pre;
            pre = pre * nums[i];
        }
        
        int post = 1;
        for (int j = nums.size() - 1; j >= 0; j--) {
            output[j] = post * output[j];
            post = post * nums[j];
        }
        return output;
    }
};
