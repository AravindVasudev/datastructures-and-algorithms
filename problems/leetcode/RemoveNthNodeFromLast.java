/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = new ListNode(-1);
        temp.next = head;
        ListNode first = temp, second = temp;

        int i = 0;
        while (second != null) {
            if (i > n) {
                first = first.next;
            }

            second = second.next;
            i++;
        }

        if (first == temp) {
            head = head.next;
        } else {
            first.next = first.next.next;
        }
        return head;
    }
}
