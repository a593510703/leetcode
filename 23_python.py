# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        x = []
        for List in lists:
            while List != None:
                x.append(List.val)
                List = List.next
        x.sort()
        ret = ans = ListNode(-1)
        for i in x:
            ret.next = ListNode(i)
            ret = ret.next
        return ans.next