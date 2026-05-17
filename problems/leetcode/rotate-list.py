# https://leetcode.com/problems/rotate-list
class Solution:
    def size(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        length = 0
        while head:
            head = head.next
            length += 1

        return length

    def find(self, head: ListNode, n: int) -> ListNode:
        """ Assumes n < len(list). """
        while n:
            head = head.next
            n -= 1

        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N = self.size(head)
        if N == 0: # 1: Empty List.
            return head
    
        k %= N
        if k == 0: # 2: No state change.
            return head

        # 3: Find rotation point.
        newEnd = self.find(head, N - k - 1)
        newHead = newEnd.next
        oldEnd = self.find(newEnd, k)

        # 4: Rotate
        oldEnd.next = head
        newEnd.next = None

        return newHead
