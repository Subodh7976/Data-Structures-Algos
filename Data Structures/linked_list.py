from dataclasses import dataclass
from typing import Any, Optional, List


@dataclass
class Node:
    data: Any 
    next: Optional['Node'] = None 

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None 

    def is_empty(self) -> bool:
        return self.head is None 

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return 
        current = self.head 
        while current.next:
            current = current.next 
        current.next = new_node
    
    def prepend(self, data: Any) -> None:
        new_node = Node(data, self.head)
        self.head = new_node 
    
    def delete_with_value(self, data: Any) -> None:
        if self.is_empty():
            return 
        if self.head.data == data:
            self.head = self.head.next 
            return 

        current = self.head 
        while current.next:
            if current.next.data == data:
                current.next = current.next.next 
                return 
            current = current.next 
    
    def find(self, data: Any) -> Optional[Node]:
        current = self.head 
        while current and current.data != data:
            current = current.next 
        return current
    
    def insert_after(self, target_data: Any, data: Any) -> None:
        new_node = Node(data)
        current = self.find(target_data)
        if current:
            new_node.next = current.next 
            current.next = new_node
    
    def insert_before(self, target_data: Any, data: Any) -> None:
        if self.is_empty():
            return 
        if self.head.data == target_data:
            self.prepend(data)

        prev = None 
        current = self.head 
        while current and current.data != target_data:
            prev = current
            current = current.next 
        if current:
            new_node = Node(data)
            new_node.next = current
            if prev:
                prev.next = new_node
            
    def to_list(self) -> List:
        elements = []
        current = self.head 
        while current:
            elements.append(current.data)
            current = current.next 
        return elements

    def __iter__(self):
        current = self.head 
        while current:
            yield current.data 
            current = current.next 
    
    def __repr__(self):
        return " -> ".join(str(data) for data in self)
    
    def reverse(self) -> None:
        prev = None 
        current = self.head 
        while current:
            next_node = current.next 
            current.next = prev 
            prev = current
            current = next_node
        self.head = prev 
