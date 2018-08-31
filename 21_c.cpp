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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *ans = new ListNode(-1);
        ListNode *p = ans;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                ans->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            else {
                ans->next = new ListNode(l2->val);
                l2 = l2->next;
            }
            ans = ans->next;
        }
        while (l1) {
            ans->next = new ListNode(l1->val);
            l1 = l1->next;
            ans = ans->next;
        }
        while (l2) {
            ans->next = new ListNode(l2->val);
            l2 = l2->next;
            ans = ans->next;
        }
        return p->next;
    }
};