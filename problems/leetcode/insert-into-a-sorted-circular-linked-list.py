# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode

        prev, cur = head, head.next
        while prev.next != head:
            # Case 1: insert b/w two nodes.
            if prev.val <= newNode.val <= cur.val:
                break

            # Case 2: When the list splits, i.e., goes from
            # a higher value to a lower value, insert the
            # newNode if it either after prev or before cur.
            if (prev.val > cur.val and
                (newNode.val > prev.val or newNode.val < cur.val)):
                break

            prev, cur = prev.next, cur.next

        # Insert new node.
        newNode.next = cur
        prev.next = newNode

        return head
