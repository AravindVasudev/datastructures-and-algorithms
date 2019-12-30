/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // Non recursive
//     public ListNode reverseList(ListNode head) {
//         ListNode prev = null, cur = head, next;
//         while (cur != null) {
//             next = cur.next;
//             cur.next = prev;
//             prev = cur;
//             cur = next;
//         }

//         return prev;
//     }

    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode newHead = reverseList(head.next);

        head.next.next = head;
        head.next = null;

        return newHead;
    }
}
