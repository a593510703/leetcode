class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        Ans = []
        def solve(now, candidates, target):
            if target < candidates[0]:
                return
            if target in candidates:
                now.append(target)
                Ans.append(list(now))
                now.remove(target)
            for i in candidates:
                x = target - i
                now.append(i)
                solve(now, candidates, x)
                now.remove(i)
            #Ans = list(set(Ans))
            return Ans

        def Print(Ans):
            ans = []
            x = []
            for x in Ans:
                x = sorted(x)
                if x not in ans:
                    ans.append(x)
            return ans
        ans = solve([], candidates, target)
        if ans == None:
            return []
        return sorted(Print(ans))