ans = []
def dfs(s, l, r, n):
    if len(s) == n * 2:
        ans.append(s)
        return
    if l < n:
        dfs(s + '(', l + 1, r, n)
    if l > r:
        dfs(s + ')', l, r + 1, n)
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans.clear()
        dfs("", 0, 0, n)
        return ans