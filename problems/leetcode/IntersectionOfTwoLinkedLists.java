/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int aLen = 0, bLen = 0;
        ListNode ptr = headA;

        while (ptr != null) {
            ptr = ptr.next;
            aLen++;
        }

        ptr = headB;
        while (ptr != null) {
            ptr = ptr.next;
            bLen++;
        }

        if (aLen < bLen) {
            ptr = headA;
            headA = headB;
            headB = ptr;
        }

        int diff = Math.abs(aLen - bLen);
        for (int i = 0; i < diff; i++) {
            headA = headA.next;
        }

        while (headA != null && headB != null) {
            if (headA == headB) {
                return headA;
            }

            headA = headA.next;
            headB = headB.next;
        }

        return null;
    }
}
