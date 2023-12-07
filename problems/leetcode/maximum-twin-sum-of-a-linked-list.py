# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
class Solution:
    def getMiddle(self, head: ListNode) -> ListNode:
      slow, fast = head, head

      while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

      return slow

    def maxPairSum(self, first: ListNode, second: ListNode) -> (ListNode, int):
      nxt, pairSum = first, 0
      if second.next:
        nxt, pairSum = self.maxPairSum(first, second.next)

      pairSum = max(pairSum, nxt.val + second.val)
      return nxt.next, pairSum

    def pairSum(self, head: Optional[ListNode]) -> int:
      return self.maxPairSum(head, self.getMiddle(head))[1]
