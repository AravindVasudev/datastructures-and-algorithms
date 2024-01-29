# https://leetcode.com/problems/lru-cache/
from dataclasses import dataclass

@dataclass
class Node:
    key: int = None
    value: int = None
    prev: "Node" = None
    nxt: "Node" = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Init hashmap.
        self.nodes = {}

        # Init doubly linked-list.
        self.head = Node()
        self.tail = Node(None, None, self.head, None)
        self.head.nxt = self.tail


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        # Move to the gotten node to the front of
        # the list.
        gotten = self.nodes[key]

        # Remove from the list.
        self.remove(gotten)

        # Add to front of the list.
        self.pushLeft(gotten)

        return gotten.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])

        # Create a node and insert in the front.
        newNode = Node(key, value)
        self.pushLeft(newNode)

        # Add to hash table.
        self.nodes[key] = newNode

        # On overflow, kick out the least recently
        # used node.
        if len(self.nodes) > self.capacity:
            toRemove = self.tail.prev

            self.remove(toRemove)
            del self.nodes[toRemove.key]

    def remove(self, node: Node) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def pushLeft(self, node: Node) -> None:
        node.prev, node.nxt = self.head, self.head.nxt
        self.head.nxt.prev = node
        self.head.nxt = node
