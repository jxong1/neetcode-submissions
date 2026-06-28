class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (auto c: tokens) {
            if (c == "+" || c == "-" || c == "*" || c == "/") {
                int num1 = stk.top();
                stk.pop();
                int num2 = stk.top();
                stk.pop();
                if (c == "+") {
                    stk.push(num1 + num2);
                }
                else if (c == "-") {
                    stk.push(num2 - num1);
                }
                else if (c == "*") {
                    stk.push(num1 * num2);
                }
                else {
                    stk.push(num2 / num1);
                }
            }
            else {
                stk.push(stoi(c));
            }
        }
        return int(stk.top());
    }
};
