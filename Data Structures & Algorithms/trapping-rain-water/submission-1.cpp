class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxLeft = height[left];
        int maxRight = height[right];
        int total = 0;
        while (left < right) {
            if (maxLeft < maxRight) {
                left++;
                total += max(0, min(maxLeft, maxRight) - height[left]);
                maxLeft = max(maxLeft, height[left]);
            }
            else {
                right--;
                total += max(0, min(maxLeft, maxRight) - height[right]);
                maxRight = max(maxRight, height[right]);
            }
        }
        return total;
    }
};
