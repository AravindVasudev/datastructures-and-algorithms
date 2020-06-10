# https://leetcode.com/problems/rotate-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (head is None) or (k is 0):
            return head
        
        length = 1
        slow, fast = head, head
        while (slow.next is not None) and (fast is not None) and (fast.next is not None):
                slow = slow.next
                fast = fast.next.next

                length += 2
                
        length -= 1 if fast is None else 0
        
        if k >= length:
            k %= length
        
        if k == 0:
            return head
        
        ptr = head
        for _ in range(length - k - 1):
            ptr = ptr.next

        last_node = ptr
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = head
        new_head = ptr.next
        ptr.next = None

        return new_head
