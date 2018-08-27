class Solution {
public:
    string convert(string s, int numRows) {
        int k = numRows * 2 - 2, len = s.length(), now = 0, Size = 0;
        char Map[1000][1000];
        k = len / k;
        for (int T = 1; T <= k + 1; T++) {
            for (int i = 0; i < numRows; i++) {
                Map[i][now] = s[Size++];
                if (Size >= len)
                    break;
            }
            now++;
            for (int i = 0; i < numRows - 2; i++) {
                Map[numRows - i - 2][now++] = s[Size++];
                if (Size >= len)
                    break;
            }
        }
        Size = 0;
        string ans;
        for (int i = 0; i < numRows; i++)
            for (int j = 0; j < now; j++) {
                if (Map[i][j] != ' ' && Map[i][j] != '\n' && Map[i][j] != '\0')
			    	ans[Size++] = Map[i][j];
		    }
	    return ans;
    }
};
