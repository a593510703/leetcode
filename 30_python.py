class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        lens = []
        Lens = []
        x = []
        Sum = 0
        for i in range(n):
            tmp = len(words[i])
            Sum += tmp
            Lens.append(tmp)
            if tmp not in lens:
                lens.append(tmp)
        lens.sort()
        i = 0
        while True:
            if i >= len(s):
                break
            flag = 0
            for j in lens:
                tmp = str(s[i:i + j])
                if tmp in words:
                    Index = words.index(tmp)
                    x.append(Index)
                    i += j
                    flag = 1
            if flag == 0:
                x.append(s[i])
                i = i + 1
        N = len(x)
        ans = []
        loc = 0
        tmp = [0] * n
        for i in range(N):
            if isinstance(x[i], str):
                tmp = [0] * (n)
                loc += 1
            else:
                tmp[x[i]] = 1
                loc += Lens[x[i]]
            if tmp[:] == [1] * n:
                ans.append(loc - Sum)
        return ans