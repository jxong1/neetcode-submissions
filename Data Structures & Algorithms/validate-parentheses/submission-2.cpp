class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (auto c: s) {
            if (c == '(' or c == '{' or c == '[') {
                stk.push(c);
            }
            else {
                if (stk.empty()) {
                    return false;
                }
                auto popped = stk.top();
                stk.pop();
                if ((c == ')' and popped == '(') or (c == '}' and popped == '{') or (c == ']' and popped == '[')) {
                    continue;
                }
                else {
                    return false;
                }
            }
        }
        return stk.empty();
    }
};
