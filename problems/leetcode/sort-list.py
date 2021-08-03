# https://leetcode.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head);
        right = self.sortList(mid);
        
        return self.merge(left, right);
    
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummyHead = tail = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
        tail.next = list1 if list1 else list2
        return dummyHead.next
    
    def getMid(self, head: ListNode) -> ListNode:
        slowPrev = slow = fast = head

        while fast is not None and fast.next is not None:
            slowPrev = slow
            slow = slow.next
            fast = fast.next.next
            
        slowPrev.next = None
        return slow
