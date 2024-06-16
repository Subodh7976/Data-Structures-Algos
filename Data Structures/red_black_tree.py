from typing import Any, Optional 


class Node:
    def __init__(self, key: Any, value: Any, color: str = "red") -> None:
        self.key = key 
        self.value = value 
        self.color = color
        self.left: Optional['Node'] = None 
        self.right: Optional['Node'] = None 
        self.parent: Optional['Node'] = None 

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value}, color-{self.color})"

class RedBlackTree:
    def __init__(self) -> None:
        self.NIL_LEAF = Node(key=None, value=None, color='black')
        self.root: Node = self.NIL_LEAF
    
    def insert(self, key: Any, value: Any) -> None:
        new_node = Node(key=key, value=value)
        self.root = self._insert(self.root, new_node)
        self._fix_insert(new_node)
    
    def _insert(self, root: Optional[Node], node: Node) -> Node:
        if root is self.NIL_LEAF:
            node.left = self.NIL_LEAF
            node.right = self.NIL_LEAF
            node.color = "red"
            return node 
        elif node.key < root.key:
            root.left = self._insert(root.left, node)
            root.left.parent = root 
        elif node.key > root.key:
            root.right = self._insert(root.right, node)
            root.right.parent = root 
        else:
            root.value = node.value 
        return root 
    
    def _fix_insert(self, node: Node) -> None:
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent 
                        self._left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left 
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent 
                else:
                    if node == node.parent.left:
                        node = node.parent 
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)
        self.root.color = "black"
    
    def delete(self, key: Any) -> None:
        node = self._search(self.root, key)
        if node == self.NIL_LEAF:
            raise KeyError(f"Key {key} not found in the red balck tree")
        self._delete_node(node)
    
    def _delete_node(self, node: Node) -> None:
        original_color = node.color 
        if node.left == self.NIL_LEAF:
            temp = node.right 
            self._transplant(node, node.right)
        elif node.right == self.NIL_LEAF:
            temp = node.left 
            self._transplant(node, node.left)
        else:
            successor = self._get_min_value_node(node.right)
            original_color = successor.color 
            temp = successor.right 
            if successor.parent == node:
                temp.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node.right 
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left 
            successor.left.parent = successor
            successor.color = node.color 
        
        if original_color == "black":
            self._fix_delete(temp)
    
    def _fix_delete(self, node: Node) -> None:
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right 
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self._left_rotate(node.parent)
                    sibling = node.parent.right 
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent 
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = "black"

    def search(self, key: Any) -> Any:
        node = self._search(self.root, key)
        if node == self.NIL_LEAF:
            raise KeyError(f"Key {key} not found in Red-Black Tree")
        return node.value

    def _search(self, node: Node, key: Any) -> Node:
        while node != self.NIL_LEAF and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def _left_rotate(self, x: Node) -> None:
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x: Node) -> None:
        y = x.left
        x.left = y.right
        if y.right != self.NIL_LEAF:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _transplant(self, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _get_min_value_node(self, node: Node) -> Node:
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def inorder_traversal(self) -> None:
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node) -> None:
        if node != self.NIL_LEAF:
            self._inorder_traversal(node.left)
            print(f"{node.key}: {node.value} ({node.color})", end=" ")
            self._inorder_traversal(node.right)
