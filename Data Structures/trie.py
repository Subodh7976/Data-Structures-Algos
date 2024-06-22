from typing import Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str) -> None:
        self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0

        char = word[depth]
        if char not in node.children:
            return False

        should_delete_child = self._delete(node.children[char], word, depth + 1)

        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0

        return False

    def __repr__(self) -> str:
        words = []
        self._collect_words(self.root, "", words)
        return f"Trie({words})"

    def _collect_words(self, node: TrieNode, prefix: str, words: list) -> None:
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

