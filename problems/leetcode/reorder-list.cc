// https://leetcode.com/problems/reorder-list/
class Solution {
private:
    static ListNode* findMiddle(ListNode* head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }

    static ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr;
        while (head) {
            ListNode* next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }

        return prev;
    }

    static void interleave(ListNode* first, ListNode* second) {
        while (second) {
            ListNode *fnext = first->next, *snext = second->next;
            first->next = second;
            second->next = fnext;
            first = fnext;
            second = snext;
        }
    }

    static void printList(ListNode* head) {
        while (head) {
            std::cout << head->val;
            if (head->next) {
                std::cout << " -> ";
            }

            head = head->next;
        }

        std::cout << std::endl;
    }

public:
    void reorderList(ListNode* head) {
        ListNode *middle = findMiddle(head);
        ListNode *second = middle->next;
        middle->next = nullptr;

        interleave(head, reverseList(second));
    }
};
