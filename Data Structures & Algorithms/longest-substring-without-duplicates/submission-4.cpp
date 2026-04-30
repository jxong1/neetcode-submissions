class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longest = 0;
        int i = 0;
        unordered_map<char, int> chars;
        while (i < s.size()) {
            char curr = s[i];
            cout << curr << " ";
            if (chars.find(curr) != chars.end()) {
                cout << i << " ";
                longest = max((int)chars.size(), longest);
                i = chars[curr] + 1;
                cout << "i: " << i;
                chars.clear();
                continue;
            }
            chars[curr] = i;
            i++;
        }
        return max(longest, (int)chars.size());
    }
};
