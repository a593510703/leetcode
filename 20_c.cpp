class Solution {
public:
    bool isValid(string s) {
        stack <int> Stack;
        char x[] = {'(', '[', '{'};
        int y[] = {1, 2, 3};
        char z[] = {')', ']', '}'};
        int len = s.length();
        if (len == 0)
            return true;
        if (len % 2)
            return false;
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < 3; j++) {
                if (s[i] == x[j])
                    Stack.push(y[j]);
            }
            for (int j = 0; j < 3; j++) {
                if (!Stack.empty() && s[i] == z[j] && Stack.top() == y[j])
                    Stack.pop();
            }
        }
        return Stack.empty();
    }
};