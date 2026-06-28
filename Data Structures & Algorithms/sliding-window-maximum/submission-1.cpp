class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> output;
        int left = 0;
        int right = 0;
        while (right < nums.size()) {
            while (!dq.empty() && nums[dq.back()] < nums[right]) {
                dq.pop_back();
            }
            dq.push_back(right);

            if (left > dq.front()) {
                dq.pop_front();
            }
                   
            if (right + 1 >= k) {
                output.push_back(nums[dq.front()]);
                left++;
            }
            right++;
        }
        return output;
    }
};
