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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode *tmp1 = head, *tmp2 = head->next->next;
        head = head->next;
        head->next = tmp1;
        head->next->next = swapPairs(tmp2);
        return head;
    }
};
