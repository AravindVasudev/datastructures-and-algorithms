# https://leetcode.com/problems/merge-k-sorted-lists/
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.mergeTwo(l, r)

    def mergeTwo(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ptr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next

            ptr = ptr.next

        ptr.next = list1 or list2
        return dummy.next
