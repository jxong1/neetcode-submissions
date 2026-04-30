class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) { return false; }

        unordered_map <char, int> s_seen;
        unordered_map <char, int> t_seen;

        for (int i = 0; i < s.size(); i++) {
            s_seen[s[i]]++;
            t_seen[t[i]]++;
        }
        return s_seen == t_seen;
    }
};
