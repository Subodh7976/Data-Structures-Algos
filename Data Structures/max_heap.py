from typing import List, Optional

class MaxHeap:
    def __init__(self):
        self.heap: List[int] = []

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2

    def _heapify_up(self, index: int) -> None:
        while index > 0 and self.heap[self._parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index: int) -> None:
        size = len(self.heap)
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, key: int) -> None:
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> Optional[int]:
        if not self.heap:
            return None
        root = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._heapify_down(0)
        return root

    def get_max(self) -> Optional[int]:
        if not self.heap:
            return None
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def __repr__(self) -> str:
        return f"MaxHeap({self.heap})"

