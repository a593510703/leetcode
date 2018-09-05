class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        Len = len(s)
        Stack = []
        for i in range(Len):
            if s[i] == '(':
                Stack.append(-1)
            else:
                if len(Stack) > 1 and Stack[-1] > 0 and Stack[-2] == -1:
                    x = Stack[-1]
                    del Stack[-1]
                    del Stack[-1]
                    Stack.append(x + 2)
                elif len(Stack) > 0 and Stack[-1] == -1:
                    del Stack[-1]
                    Stack.append(2)
                else:
                    Stack.append(-2)
            while len(Stack) > 2 and Stack[-1] == -2:
                if Stack[-3] == -1 and Stack[-2] > 0:
                    Stack[-3] = Stack[-2] + 2
                    del Stack[-1]
                    del Stack[-1]
                else:
                    break
            while len(Stack) > 1 and Stack[-1] > 0 and Stack[-2] > 0:
                Stack[-2] += Stack[-1]
                del Stack[-1]
        ans = 0
        for i in Stack:
            if i > ans:
                ans = i
        return ans