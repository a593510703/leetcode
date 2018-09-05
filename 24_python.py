# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0);
        p.next = head;
        while p.next != None and p.next.next != None:
            p.next.next.next, p.next.next, p.next, p = \
            p.next, p.next.next.next, p.next.next, p.next
        return dummy.next