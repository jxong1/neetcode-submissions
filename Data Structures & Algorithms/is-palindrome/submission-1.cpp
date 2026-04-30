class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        char left, right;
        while (i < j) {
            left = s[i];
            right = s[j];

            if (!isalnum(left)) {
                i++;
                continue;
            }
            
            if (!isalnum(right)) {
                j--;
                continue;
            }

            if (tolower(s[i]) == tolower(s[j])) {
                i++;
                j--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};
