from dataclasses import dataclass
from typing import Any, List, Optional, Tuple 


@dataclass
class Node:
    key: Any 
    value: Any 
    next: Optional['Node'] = None 

class HashTable:
    def __init__(self, initial_capacity: int = 8) -> None:
        self._capacity = initial_capacity
        self._size = 0 
        self._buckets: List[Optional[Node]] = [None] * self._capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity
    
    def insert(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        node = self._buckets[index]

        if node in None:
            self._buckets[index] = Node(key, value)
            self._size += 1
            return 
        
        prev = None 
        while node:
            if node.key == key:
                node.value = value 
                return 
            prev = node 
            node = node.next 

        prev.next = Node(key, value)
        self._size += 1

        if self._size / self._capacity > 0.7:
            self._resize()
    
    def _resize(self) -> None:
        new_capacity = self._capacity * 2
        new_buckets = [None] * new_capacity
        old_buckets = self._buckets

        self._capacity = new_capacity
        self._buckets = new_buckets
        self._size = 0

        for node in old_buckets:
            while node:
                self.insert(node.key, node.value)
                node = node.next 

    def access(self, key: Any) -> Any:
        index = self._hash(key)
        node = self._buckets[index]

        while node:
            if node.key == key:
                return node.value 
            node = node.next 

        raise KeyError(f"Key {key} not found in the hash table")
    
    def delete(self, key: Any) -> None:
        index = self._hash(key)
        node = self._buckets[index]
        prev = None 

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next 
                else:
                    self._buckets[index] = node.next 
                self._size -= 1
                return 
            prev = node 
            node = node.next 
        
        raise KeyError(f"Key {key} not found in the HashTable")
    
    def search(self, key: Any) -> bool:
        index = self._hash(key)
        node = self._buckets[index]

        while node:
            if node.key == key:
                return True 
            node = node.next 

        return False 
    
    def size(self) -> int:
        return self._size
    
    def __iter__(self):
        for bucket in self._buckets:
            node = bucket
            while node:
                yield (node.key, node.value)
                node = node.next 
    
    def __repr__(self):
        return "HashTable(" + ", ".join(f"{key}: {value}" for key, value in self) + ")"
    