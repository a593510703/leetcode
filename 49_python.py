class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        Dict = {}
        ans = []
        for string in strs:
            Str = list(string)
            Str.sort()
            Str = ''.join(Str)
            if Str not in Dict:
                Dict[Str] = len(ans)
                ans.append([string])
            else:
                ans[Dict[Str]].append(string)
        return ans