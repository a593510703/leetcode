# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = tmp = ListNode(0)
        k = 0
        while l1 and l2:
            x = l1.val + l2.val + k
            if x >= 10:
                k = 1
                x = x - 10
            else:
                k = 0
            ret.next = ListNode(x)
            l1 = l1.next
            l2 = l2.next
            ret = ret.next
        aft = l1 or l2
        while aft:
            x = aft.val + k
            if x >= 10:
                k = 1
                x = x - 10
            else:
                k = 0
            ret.next = ListNode(x)
            ret = ret.next
            aft = aft.next
        if k == 1:
            ret.next = ListNode(1)
        return tmp.next