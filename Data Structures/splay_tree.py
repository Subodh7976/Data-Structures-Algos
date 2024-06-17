from typing import Optional, Any

class Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value})"

class SplayTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def _right_rotate(self, x: Node) -> None:
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, x: Node) -> None:
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _splay(self, node: Node) -> None:
        while node.parent:
            if not node.parent.parent:
                if node.parent.left == node:
                    self._right_rotate(node.parent)
                else:
                    self._left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.left == node.parent:
                self._right_rotate(node.parent.parent)
                self._right_rotate(node.parent)
            elif node.parent.right == node and node.parent.parent.right == node.parent:
                self._left_rotate(node.parent.parent)
                self._left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.right == node.parent:
                self._right_rotate(node.parent)
                self._left_rotate(node.parent)
            else:
                self._left_rotate(node.parent)
                self._right_rotate(node.parent)

    def _search_tree_helper(self, node: Optional[Node], key: Any) -> Optional[Node]:
        if not node or key == node.key:
            return node
        if key < node.key:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def search(self, key: Any) -> Any:
        node = self._search_tree_helper(self.root, key)
        if node:
            self._splay(node)
            return node.value
        raise KeyError(f"Key {key} not found in Splay Tree")

    def insert(self, key: Any, value: Any) -> None:
        node = Node(key, value)
        y = None
        x = self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        self._splay(node)

    def _transplant(self, u: Node, v: Optional[Node]) -> None:
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, key: Any) -> None:
        node = self._search_tree_helper(self.root, key)
        if not node:
            raise KeyError(f"Key {key} not found in Splay Tree")
        self._splay(node)
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            if y.parent != node:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def _minimum(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self) -> None:
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Optional[Node]) -> None:
        if node:
            self._inorder_traversal(node.left)
            print(f"{node.key}: {node.value}", end=" ")
            self._inorder_traversal(node.right)

