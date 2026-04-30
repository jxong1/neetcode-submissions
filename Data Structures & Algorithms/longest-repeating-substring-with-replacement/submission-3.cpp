class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int right = 0;
        int maxFreq = 1;
        int res = 0;
        unordered_map<char, int> counts;
        
        for (int right = 0; right < s.size(); right++) {
            counts[s[right]]++;
            maxFreq = max(counts[s[right]], maxFreq);

            while ((right - left + 1 - maxFreq) > k) {
                counts[s[left]]--;
                left++;
            }
            res = max(res, right - left + 1);
        }
        return res;
    }
};
