# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummyHead = Node(0)
        ptr = dummyHead
        mapping = {}
        while head is not None:
            duplicate = Node(head.val)
            duplicate.next, duplicate.random = head.next, head.random
            
            mapping[head] = duplicate
            
            ptr.next = duplicate
            head = head.next
            ptr = ptr.next
            
        dummyHead = dummyHead.next
        ptr = dummyHead
        while ptr is not None:
            if ptr.random is not None:
                ptr.random = mapping[ptr.random]
            
            ptr = ptr.next
            
        return dummyHead
