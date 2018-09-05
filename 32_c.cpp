class Solution {
public:
    int longestValidParentheses(string s) {
		int len = s.length(), ans = 0, size = 0, Stack[100010];
		memset(Stack, 0, sizeof(Stack));
		for (int i = 0; i < len; i++) {
			if (s[i] == '(') {
				Stack[++size] = -1;
			}
			else {
				if (Stack[size] > 0 && Stack[size - 1] == -1) {
					Stack[size - 1] = Stack[size] + 2;
					size--;
				}
				else if (Stack[size] == -1) {
					Stack[size] = 2;
				}
				else
					Stack[++size] = -2;
			}
			while (Stack[size] == -2 && size > 2) {
				if (Stack[size - 2] == -1 && Stack[size - 1] > 0) {
					Stack[size - 2] = Stack[size - 1] + 2;
					size -= 2;
				}
                else
                    break;
			}
			while (Stack[size] > 0) {
				if (Stack[size - 1] > 0) {
					Stack[size - 1] += Stack[size];
					size--;
				}
				else
					break;
			}
		}
		for (int i = 1; i <= size; i++)	
			if (Stack[i] > ans)
				ans = Stack[i];
		return ans;
    }
};
