/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode dummy = new ListNode(-1);
        ListNode ptr = dummy;

        boolean done = false;
        do {
            int selected = -1, doneCount = 0;
            for (int i = 0; i < lists.length; i++) {
                if (lists[i] == null) {
                    doneCount++;
                    continue;
                }

                if (selected == -1 || (lists[selected].val > lists[i].val)) {
                    selected = i;
                }
            }

            done = (lists.length == doneCount);

            if (!done) {
                ptr.next = lists[selected];
                lists[selected] = lists[selected].next;
                ptr = ptr.next;
            }
        } while (!done);

        return dummy.next;
    }
}
