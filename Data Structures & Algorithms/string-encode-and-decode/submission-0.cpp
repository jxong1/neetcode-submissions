class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for (auto str: strs) {
            for (char s: str) {
                int ord = s;
                encoded += to_string(s);
                encoded += " ";
            }
            encoded += "#";
        }
        cout << encoded;
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        string decoded_str = "";
        string char_int = "";
        for (auto ch: s) {
            if (ch == ' ') {
                decoded_str += (char)stoi(char_int);
                char_int = "";
            }
            else if (ch == '#') {
                decoded.push_back(decoded_str);
                decoded_str = "";
            }
            else {
                char_int += ch;
            }
        }
        return decoded;
    }
};
