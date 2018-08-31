# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = q = head
        cnt = 0
        while p != None:
            p = p.next
            cnt += 1
        if cnt == 0:
            return None
        if cnt == n:
            return head.next
        cnt = cnt - n - 1
        for i in range(cnt):
            q = q.next
        q.next = q.next.next
        return head