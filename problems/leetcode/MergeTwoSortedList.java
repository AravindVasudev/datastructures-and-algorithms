/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode merged = null, ptr = null;
        
        if (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                merged = l1;
                l1 = l1.next;
            } else {
                merged = l2;
                l2 = l2.next;
            }
        } else if (l1 != null) {
            merged = l1;
            l1 = l1.next;
        } else if (l2 != null) {
            merged = l2;
            l2 = l2.next;
        }
        
        ptr = merged;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                ptr.next = l1;
                l1 = l1.next;
            } else {
                ptr.next = l2;
                l2 = l2.next;
            }
            
            ptr = ptr.next;
        }
        
        while (l1 != null) {
            ptr.next = l1;
            ptr = ptr.next;
            l1 = l1.next;
        }
        
        while (l2 != null) {
            ptr.next = l2;
            ptr = ptr.next;
            l2 = l2.next;
        }
        
        return merged;
    }
}