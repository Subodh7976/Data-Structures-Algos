from typing import List

class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self._build(data)

    def _build(self, data: List[int]) -> None:
        # Initialize leaves of the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, value: int) -> None:
        # Update leaf node
        index += self.n
        self.tree[index] = value
        # Update the ancestors
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def range_query(self, left: int, right: int) -> int:
        # Perform the range query
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

    def __repr__(self) -> str:
        return f"SegmentTree({self.tree})"
