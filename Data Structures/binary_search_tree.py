from typing import Any, Optional, List


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key 
        self.value = value 
        self.left: Optional['Node'] = None 
        self.right: Optional['Node'] = None 

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value})"

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None 
    
    def insert(self, key: Any, value: Any) -> None:
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_recursive(self.root, key, value)
    
    def _insert_recursive(self, node: Node, key: Any, value: Any) -> None:
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert_recursive(node.right, key, value)
        else:
            node.value = value 
    
    def search(self, key: Any) -> Any:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[Node], key: Any) -> bool:
        if node is None:
            raise KeyError(f"Key {key} not found in BST")
        if key == node.key:
            return node.value 
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def delete(self, key: Any) -> None:
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node: Optional[Node], key: Any) -> Optional[Node]:
        if node is None:
            raise KeyError(f"Key {key} not in BST")

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right 
            elif node.right is None:
                return node.left 

            min_larger_node = self._get_min(node.right)
            node.key, node.value = min_larger_node.key, min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.key)
        
        return node 
    
    def _get_min(self, node: Node) -> Node:
        current = node 
        while current.left is not None:
            current = current.left 
        
        return current

    def inorder(self) -> List[Any]:
        result = []
        self._inorder_recursive(self.root, result)
        return result 
    
    def _inorder_recursive(self, node: Optional[Node], result: List[Any]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)
    
    def __repr__(self) -> str:
        return "BinarySearchTree(" + ", ".join(f"{key}: {value}" for key, value in self.inorder()) + ")"
    
            