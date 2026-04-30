class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_water = 0;
        int left = 0, right = heights.size() - 1;
        while (left < right) {
            int left_h = heights[left], right_h = heights[right];
            int area = (right - left) * min(right_h, left_h);
            max_water = max(area, max_water);
            if (left_h > right_h) {
                right--;
            }
            else {
                left++;
            }
        }
        return max_water;
    }
};
