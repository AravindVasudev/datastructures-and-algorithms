# https://leetcode.com/problems/odd-even-linked-list/
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not (head and head.next):
        return head

      odd = ListNode()
      evenHead = even = ListNode()
      cur, index = head, 1

      while cur:
        if index % 2 == 1:
          odd.next = cur
          odd = odd.next
        else:
          even.next = cur
          even = even.next

        cur = cur.next
        index += 1

      even.next = None
      odd.next = evenHead.next

      return head
