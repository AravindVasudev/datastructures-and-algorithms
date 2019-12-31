// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        Stack<Integer> stack = new Stack<>();

        while (head != null) {
            stack.push(head.val);
            head = head.next;
        }

        int twoPow = 1, num = 0;
        while (!stack.isEmpty()) {
            num += stack.pop() * twoPow;
            twoPow <<= 1;
        }

        return num;
    }
}
