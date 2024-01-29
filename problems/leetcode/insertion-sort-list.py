# https://leetcode.com/problems/insertion-sort-list/
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        sortedList = ListNode(float("-inf"))
        ptr = head
    
        # Walk through every node and add it to the
        # sorted list.
        while ptr:
            nxt = ptr.next
            self.insert(sortedList, ptr)
            ptr = nxt

        return sortedList.next

    def insert(self, head, node):
        """ Inserts node into the sorted list `head`. """
        prev, cur = head, head.next

        while cur:
            # Found in-between position.
            if prev.val <= node.val <= cur.val:
                break

            prev, cur = prev.next, cur.next

        # Insert the node in-between.
        prev.next = node
        node.next = cur
