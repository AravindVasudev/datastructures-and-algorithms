"""
A simple in-memory B-Tree implementation for learning purposes.
Based on CLRS 3rd edition, Chapter 18.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Node:
    """ Comparable Node """
    # TODO: Update key with a comparable type
    key: int
    value: Any

    def __lt__(self, other: Node) -> bool:
        return self.key < other.key


@dataclass
class BTreeNode:
    """ B-Tree Node """
    keys: List[Node] = field(default_factory=list)
    c: List[BTreeNode] = field(default_factory=list)
    leaf: bool = True

    def __str__(self) -> str:
        return f"[keys: {self.keys} leaf: {self.leaf} child: {len(self.c)}]\n" \
            + "\n".join([str(child) for child in self.c])

class BTree:
    """
    B-Tree Implementation
    """
    def __init__(self, t: int = 2):
        """
        Initializes B-Tree.

        :param t: Branching factor. For every node,
            t <= number of child <= 2t
            t - 1 <= number of keys <= 2t - 1

        """
        self.root = BTreeNode()
        self.t = t

    def search(self, x: int, bNode: BTreeNode = None) -> Node:
        """
        Searches key x in the given B-Tree node.

        :param x: exact key to search.
        :param bNode: B-Tree node to search from. Default value is `self.root`.

        :return: Node if found else None
        """

        # Default value
        if bNode is None:
            bNode = self.root

        # Linear search
        # TODO: Test out binary search here.
        i: int = 0
        while i < len(bNode.keys) and x > bNode.keys[i].key:
            i += 1

        if i < len(bNode.keys) and x == bNode.keys[i].key: # if found
            return bNode.keys[i]
        elif bNode.leaf: # if node is leaf
            return None
        else:
            # NOTE: bNode.c[i] have to be read from the disk here irl
            return self.search(x, bNode.c[i]) # Search ith child

    def insert(self, node: Node) -> None:
        """
        Inserts node into the B-Tree.

        :param node: Node to insert.
        """

        if len(self.root.keys) == 2 * self.t - 1:
            s = BTreeNode(c=[self.root], leaf=False)
            self.root = s

            self._splitChild(self.root, 0)

        self._insertNonFull(self.root, node)

    def _splitChild(self, bNode: BTreeNode, i: int) -> None:
        """
        Helper method that splits bNode.c[i] into two childs.
        bNode.c[i] is assumed to be a full child.
        Both bNode and bNode.c[i] are assumed to be in-memory irl
        implementation.

        :param bNode: B-Tree Parent node
        :param i: index of the full child in bNode.c
        """

        y = bNode.c[i]
        z = BTreeNode(leaf=y.leaf)

        bNode.keys.insert(i, y.keys[self.t - 1])
        bNode.c.insert(i + 1, z)

        z.keys = y.keys[self.t:]
        y.keys = y.keys[:self.t - 1]

        if not y.leaf:
            z.c = y.c[self.t:]
            y.c = y.c[:self.t]
        
        # Disk write bNode, y, and z here irl.

    def _insertNonFull(self, bNode: BTreeNode, node: Node) -> None:
        """
        Helper method to node into a non-full bNode.
        bNode is assumed to be not full.

        :param bNode: B-Tree node to insert into.
        :param node: Node to insert.
        """

        i = len(bNode.keys) - 1
        if bNode.leaf:
            bNode.keys.append(None)
            while i >= 0 and node.key < bNode.keys[i].key:
                bNode.keys[i+1] = bNode.keys[i]
                i -= 1

            bNode.keys[i+1] = node
            # Disk write bNode irl
        else:
            while i >= 0 and node.key < bNode.keys[i].key:
                i -= 1

            i += 1

            # Disk read bNode.c[i] here irl
            if len(bNode.c[i].keys) == 2 * self.t - 1:
                self._splitChild(bNode, i)
                if node.key > bNode.keys[i].key:
                    i += 1

            self._insertNonFull(bNode.c[i], node)

    def __str__(self) -> str:
        return str(self.root)


if __name__ == "__main__":
    # Init
    dataStore = BTree()

    # Insert
    for i in range(10, 0, -1):
        dataStore.insert(Node(i, f"Foo-{i}"))

    # Print current state
    print("=== B-Tree ===")
    print(dataStore)
    print()

    # Search
    print("=== Search Queries ===")
    print("Search(7):", dataStore.search(7))
    print("Search(5):", dataStore.search(5))
    print("Search(1):", dataStore.search(1))
    print("Search(11):", dataStore.search(11))
