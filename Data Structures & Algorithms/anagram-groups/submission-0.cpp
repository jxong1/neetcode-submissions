class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, int> seen;
        vector<vector<string>> anas;
        int next_ind = 0;
        for (string str: strs) {
            string ana = str;
            sort(ana.begin(), ana.end());
            cout << ana << "\n";
            if (seen.find(ana) != seen.end()) {
                anas[seen[ana]].push_back(str);
            }
            else {
                anas.push_back({str});
                seen.insert({ana, next_ind});
                next_ind++;
            }
        }
        return anas;
    }
};
