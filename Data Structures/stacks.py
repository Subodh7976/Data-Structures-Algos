from dataclasses import dataclass 
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next: Optional['Node'] = None 

class Stack:
    def __init__(self) -> None:
        self.top: Optional[Node] = None 
        self._size: int = 0

    def is_empty(self) -> bool:
        return self.top is None 

    def push(self, data: Any) -> None:
        new_node = Node(data, self.top) 
        self.top = new_node
        self._size += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top 
        self.top = self.top.next 
        self._size -= 1
        return popped_node.data 
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data 

    def size(self) -> int:
        return self._size 

    def __iter__(self):
        current = self.top 
        while current:
            yield current.data 
            current = current.next 

    def __repr__(self):
        return " -> ".join(str(data) for data in self)
    


