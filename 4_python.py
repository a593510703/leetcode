class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = 0
        n = len(nums1)
        m = len(nums2)
        tmp = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i = i + 1
            else:
                tmp.append(nums2[j])
                j = j + 1
        while i < n:
            tmp.append(nums1[i])
            i = i + 1
        while j < m:
            tmp.append(nums2[j])
            j = j + 1
        Len = n + m
        if Len % 2 == 0:
            return (tmp[(Len - 1) // 2] + tmp[(Len + 1) // 2]) / 2
        else:
            return float(tmp[Len // 2])