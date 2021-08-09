from typing import List, Optional

class MinHeap:
    """
    MinHeap Implementation
    """

    def __init__(self):
        self.heap: List[int] = []

    def swap(self, firstPos, secondPos):
        self.heap[firstPos], self.heap[secondPos] = \
            self.heap[secondPos], self.heap[firstPos]

    def __str__(self) -> str:
        return str(self.heap)

    def getLeftChildIndex(self, pos: int) -> int:
        return 2 * pos + 1

    def getRightChildIndex(self, pos: int) -> int:
        return 2 * pos + 2

    def getParentIndex(self, pos: int) -> int:
        return (pos - 1) // 2

    def hasParent(self, pos: int) -> bool:
        return self.getParentIndex(pos) >= 0

    def hasLeftChild(self, pos: int) -> bool:
        return self.getLeftChildIndex(pos) < len(self.heap)

    def hasRightChild(self, pos: int) -> bool:
        return self.getRightChildIndex(pos) < len(self.heap)

    def parent(self, pos: int) -> int:
        return self.heap[self.getParentIndex(pos)]

    def leftChild(self, pos: int) -> int:
        return self.heap[self.getLeftChildIndex(pos)]

    def rightChild(self, pos: int) -> int:
        return self.heap[self.getRightChildIndex(pos)]

    def peek(self) -> Optional[int]:
        return self.heap[0] if len(heap) else None

    def poll(self) -> Optional[int]:
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minItem: int = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown()

        return minItem

    def add(self, item: int) -> None:
        self.heap.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heap) - 1
        while self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and \
                    self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)

            if self.heap[index] < self.heap[smallerChildIndex]:
                break

            self.swap(index, smallerChildIndex)
            index = smallerChildIndex


if __name__ == "__main__":
    heap: MinHeap = MinHeap()
    for i in range(10, 0, -1):
        print(f"Adding {i} to the heap")
        heap.add(i)

    print(heap)

    for i in range(11):
        print(heap.poll())
