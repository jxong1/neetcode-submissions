class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size()) {
            return "";
        }

        unordered_map<char, int> want;
        unordered_map<char, int> seen;
        int matches = 0;
        int left = 0;
        string res = "";
        int resLen = INT_MAX;
        for (auto c: t) {
            want[c]++;
            cout << "inserted: " << c << " ";
        }

        for (int right = 0; right < s.size(); right++) {
            auto c = s[right];
            seen[c]++;
            if (want.find(c) != want.end() and seen[c] == want[c]) {
                matches++;
            }

            while (matches == want.size()) {
                if ((right - left + 1) < resLen) {
                    res = s.substr(left, right - left + 1);
                    resLen = (right - left + 1);
                }
                auto c = s[left];
                seen[c]--;
                if (want.find(c) != want.end() and seen[c] < want[c]) {
                    matches--;
                }
                left++;
            }
        }
        return res;
    }
};
