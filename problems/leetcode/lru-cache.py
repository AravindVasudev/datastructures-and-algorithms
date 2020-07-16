# https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key, value, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.next = nxt
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        
        # Setup doubly linked list
        self.linked_list_head = Node(None, None)
        self.linked_list_tail = Node(None, None, None, self.linked_list_head)
        
        self.linked_list_head.next = self.linked_list_tail
        
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        curNode = self.map[key]
        
        # Remove from list
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev
        
        # Add to front
        curNode.next = self.linked_list_head.next
        curNode.next.prev = curNode
        
        self.linked_list_head.next = curNode
        curNode.prev = self.linked_list_head
        
        return curNode.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.get(key)
            return

        if len(self.map) >= self.capacity:
            nodeToEvict = self.linked_list_tail.prev
            
            # Remove the node from list
            self.linked_list_tail.prev = nodeToEvict.prev
            nodeToEvict.prev.next = self.linked_list_tail
            
            
            # Remove from map
            del self.map[nodeToEvict.key]
        
        #  Add to front
        curNode = Node(key, value, self.linked_list_head.next, self.linked_list_head)
        self.linked_list_head.next = curNode
        curNode.next.prev = curNode
        
        # Add to map
        self.map[key] = curNode
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
