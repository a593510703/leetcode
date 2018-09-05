class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        while True:
            if i >= n:
                break
            if nums[i] == val:
                n -= 1
                t = nums[i]
                nums[i] = nums[n]
                nums[n] = t
            else:
                i += 1
        return n