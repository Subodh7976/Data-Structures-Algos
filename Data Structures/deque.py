from dataclasses import dataclass
from typing import Any, Optional 


@dataclass 
class Node:
    data: Any
    next: Optional['Node'] = None 
    prev: Optional['Node'] = None 

class Deque:
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None 
        self._size: int = 0

    def is_empty(self) -> bool:
        return self.front is None 

    def add_front(self, data: Any) -> None:
        new_node = Node(data, next=self.front)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            assert self.front is not None
            self.front.prev = new_node
            self.front = new_node
        self._size += 1
    
    def add_rear(self, data: Any) -> None:
        new_node = Node(data, prev=self.rear)
        if self.is_empty():
            self.front = self.rear = new_node 
        else:
            assert self.rear is not None
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def remove_front(self) -> Any:
        if self.is_empty():
            raise IndexError("remove from empty deque")
        assert self.front is not None
        data = self.front.data 
        self.front = self.front.next 
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self._size += 1
        return data

    def remove_rear(self) -> Any:
        if self.is_empty():
            raise IndexError("remove from an empty deque")
        assert self.rear is not None
        data = self.rear.data
        self.rear = self.rear.prev 
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        self._size += 1
        return data
    
    def peek_front(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty deque")
        assert self.front is not None
        return self.front.data
    
    def peek_rear(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty deque")
        assert self.rear is not None 
        return self.rear.data

    def size(self) -> int:
        return self._size
    
    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return " <-> ".join(str(data) for data in self)
