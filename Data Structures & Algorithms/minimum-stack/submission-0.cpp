class MinStack {
    private:
        int topInd;
        vector<int> data;
        vector<int> mins;

    public:
        MinStack() {
            topInd = -1;
        }
        
        void push(int val) {
            data.push_back(val);
            if (topInd == -1 || val < mins[topInd]) {
                mins.push_back(val);
            }
            else {
                mins.push_back(mins[topInd]);
            }
            topInd++;
        }
        
        void pop() {
            if (topInd >= 0) {
                data.pop_back();
                mins.pop_back();
                topInd--;
            }
        }
        
        int top() {
            return data[topInd];
        }
        
        int getMin() {
            return mins[topInd];
        }
};
