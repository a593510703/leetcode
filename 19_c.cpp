/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode &p = *head, *q;
        q = head;
        int cnt = 0;
        while (q != NULL) {
            q = q->next;
            cnt++;
        }
        if (cnt == 1)
            return NULL;
        if (cnt == n)
            return p.next;
        cnt = cnt - n - 1;
        for (int i = 0; i < cnt; i++) {
            head = head->next;
        }
        head->next = head->next->next;
        return &p;
    }
};