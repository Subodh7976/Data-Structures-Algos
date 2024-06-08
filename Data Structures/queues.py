from dataclasses import dataclass
from typing import Any, Optional, List 


@dataclass
class Node:
    data: Any 
    next: Optional['Node'] = None 

class Queue:
    def __init__(self) -> None:
        self.front: Optional[Node] = None 
        self.rear: Optional[Node] = None 
        self._size: int = 0
    
    def is_empty(self) -> bool:
        return self.front is None 
    
    def enqueue(self, data: Any) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node 
        else:
            assert self.rear is not None 
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert self.front is not None 
        dequeued_node = self.front
        self.front = self.front.next 
        if self.front is None:
            self.rear = None
        self._size -= 1
        return dequeued_node.data 

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        assert self.front is not None 
        return self.front.data 
    
    def size(self) -> int:
        return self._size 
    
    def __iter__(self):
        current = self.front 
        while current:
            yield current.data 
            current = current.next 
    
    def __repr__(self):
        return " <- ".join(str(data) for data in self)
    