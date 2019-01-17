class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []
        result.append([])
        for i, num in enumerate(nums):
            current_result = []
            for item in result:
                for j in range(i + 1):
                    if j > 0 and num == item[j - 1]:
                        break
                    tmp = item[:]
                    tmp.insert(j, num)
                    current_result.append(tmp)
            result = current_result
        return result
                    