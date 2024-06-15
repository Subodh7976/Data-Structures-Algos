from typing import Any, Optional 

class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key 
        self.value =  value 
        self.left: Optional['Node'] = None 
        self.right: Optional['Node'] = None 
        self.height = 1

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value}, height={self.height})"

class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None 
    
    def insert(self, key: Any, value: Any) -> None:
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, node: Optional[Node], key: Any, value: Any) -> Node:
        if node is None:
            return Node(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node 
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        
        if balance < -1 and key < node.right.key:
            return self._left_rotate(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node 
    
    def delete(self, key: Any) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[Node], key: Any) -> Optional[Node]:
        if node is None:
            return node 
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right 
            elif node.right is None:
                return node.left 
            
            temp = self._get_min_value_node(node.right)
            node.key, node.value = temp.key, temp.value
            node.right = self._delete(node.right, temp.key)
        
        if node is None:
            return node 
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._left_rotate(node)
        
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node 
    
    def search(self, key: Any) -> Any:
        node = self._search(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found in AVL Tree")
        return node.value 
    
    def _search(self, node: Optional[Node], key: Any) -> Optional[Node]:
        if node is None or node.key == key:
            return node 
        
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def _left_rotate(self, z: Node) -> Node:
        y = z.right 
        T2 = y.left 
        y.left = z 
        z.rigth = T2 
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y 
    
    def _right_rotate(self, z: Node) -> Node:
        y = z.left 
        T3 = y.right 
        y.right = z 
        z.left = T3 
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        z.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y 
    
    def _get_height(self, node: Optional[Node]) -> int:
        if node is None:
            return 0 
        return node.height 
    
    def _get_balance(self, node: Optional[Node]) -> int:
        if node is None:
            return 0 
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _get_min_value_node(self, node: Node) -> Node:
        current = node 
        while current.left is not None:
            current = current.left 
        return current
    
    def inorder_traversal(self) -> None:
        self._inorder_traversal(self.root)
    
    def _inorder_traversal(self, node: Optional[Node]) -> None:
        if node: 
            self._inorder_traversal(node.left)
            print(f"{node.key}: {node.value}", end=" ")
            self._inorder_traversal(node.right)
            