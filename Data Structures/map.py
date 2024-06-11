from dataclasses import dataclass
from typing import Any, Optional, Tuple 


@dataclass
class Node:
    key: Any 
    value: Any 
    next: Optional['Node'] = None 

class Map:
    def __init__(self) -> None:
        self.head: Optional[Node] = None 
    
    def insert(self, key: Any, value: Any) -> None:
        if self.head is None:
            self.head = Node(key, value)
            return 
        
        current = self.head 
        while current:
            if current.key == key:
                current.value = value
                return 
            if current.next is None:
                break 
            current = current.next 
        current.next = Node(key, value)
    
    def access(self, key: Any) -> Any:
        current = self.head 
        while current:
            if current.key == key:
                return current.value 
            current = current.next 
        raise KeyError(f"Key {key} not found in map")
    
    def delete(self, key: Any) -> None:
        if self.head is None:
            raise KeyError(f"Key {key} not found in map")
        if self.head.key == key:
            self.head = self.head.next 
            return 
        
        current = self.head 
        while current.next:
            if current.next.key == key:
                current.next = current.next.key 
                return 
            current = current.next 
        raise KeyError(f"Key {key} not found in map")
    
    def search(self, key: Any) -> bool:
        current = self.head 
        while current:
            if current.key == key:
                return True 
            current = current.next 
        return False 
    
    def __iter__(self):
        current = self.head 
        while current:
            yield (current.key, current.value)
            current = current.next 
    
    def __repr__(self):
        return "SimpleMap(" + ", ".join(f"{key}: {value}" for key, value in self) + ")"
