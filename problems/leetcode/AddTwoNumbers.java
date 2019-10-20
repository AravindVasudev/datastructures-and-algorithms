/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbers(l1, l2, new ListNode(0));
    }

    private ListNode addTwoNumbers(ListNode l1, ListNode l2, ListNode l3) {
        if (l1 == null && l2 == null) {
            return l3.val == 0 ? null : l3;
        }

        if (l1 != null) {
            l3.val += l1.val;
            l1 = l1.next;
        }

        if (l2 != null) {
            l3.val += l2.val;
            l2 = l2.next;
        }

        int carryOver = l3.val / 10;
        l3.val = l3.val % 10;

        l3.next = addTwoNumbers(l1, l2, new ListNode(carryOver));
        return l3;
    }
}
