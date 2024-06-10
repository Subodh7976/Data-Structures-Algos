from typing import Any, List, Tuple 


class PriorityQueue:
    def __init__(self) -> None:
        self._heap: List[Tuple[int, Any]] = []
        
    def is_empty(self) -> bool:
        return len(self._heap) == 0
    
    def _parent(self, index: int) -> int:
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        return 2 * index + 2
    
    def _heapify_up(self, index: int) -> None:
        while index > 0 and self._heap[index][0] < self._heap[self._parent(index)][0]:
            self._heap[index], self._heap[self._parent(index)] = self._heap[self._parent(index)], self._heap[index]
            index = self._parent(index)
    
    def _heapify_down(self, index: int) -> None:
        smallest = index 
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self._heap) and self._heap[left][0] < self._heap[smallest][0]:
            smallest = left 
        
        if right < len(self._heap) and self._heap[right][0] < self._heap[smallest][0]:
            smallest = right 

        if smallest != index:
            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            self._heapify_down(smallest)
    
    def enqueue(self, priority: int, item: Any) -> None:
        self._heap.append((priority, item))
        self._heapify_up(len(self._heap) - 1)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        item = self._heap[0][1]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._heapify_down(0)
        return item 
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._heap[0][1]
    
    def size(self) -> int:
        return len(self._heap)
    
    def __iter__(self):
        return (item for priority, item in sorted(self._heap))
    
    def __repr__(self):
        return "PriorityQueue(" + ", ".join(f"({priority}, {item})" for priority, item in self._heap) + ")"
    