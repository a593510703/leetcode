class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.length() == 0)
            return 0;
        for (int sta = 0; sta < haystack.length(); sta++) {
            int cnt = 0;
            for (int i = 0; i < needle.length(); i++) {
                if (haystack[sta + i] == needle[i]) {
                    cnt++;
                }
            }
            if (cnt == needle.length())
                return sta;
        }
        return -1;
    }
};	
