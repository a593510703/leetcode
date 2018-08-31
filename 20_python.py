class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Stack = []
        g = ('(', ')', '[', ']', '{', '}')
        for c in s:
            for i in range(0, 3):
                if c == g[i * 2]:
                    Stack.append(i)
                elif c == g[i * 2 + 1]:
                    if len(Stack) == 0:
                        return False
                    if Stack[-1] == i:
                        del Stack[-1]
                    else:
                        return False;
        if len(Stack) == 0:
            return True
        return False