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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size(), Size = 0, a[10010];
        for (int i = 0; i < n; i++) {
            ListNode * list = lists[i];
            while (list != NULL) {
                a[++Size] = list->val;
                list = list->next;
            }
        }
        sort(a + 1, a + 1 + Size);
        ListNode *ans = new ListNode(-1);
        ListNode *p = ans;
        for (int i = 1; i <= Size; i++) {
            ans->next = new ListNode(a[i]);
            ans = ans->next;
        }
        return p->next;
    }
};
