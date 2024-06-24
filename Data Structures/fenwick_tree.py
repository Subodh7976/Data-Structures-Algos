from typing import List

class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """
        Updates the value at the given index by delta.
        
        Parameters:
        index (int): The index to update (1-based index).
        delta (int): The value to add at the given index.
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        """
        Computes the prefix sum from the start to the given index.
        
        Parameters:
        index (int): The index up to which to compute the prefix sum (1-based index).
        
        Returns:
        int: The prefix sum from the start to the given index.
        """
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left: int, right: int) -> int:
        """
        Computes the sum of elements in the range [left, right].
        
        Parameters:
        left (int): The left bound of the range (1-based index).
        right (int): The right bound of the range (1-based index).
        
        Returns:
        int: The sum of elements in the range [left, right].
        """
        return self.query(right) - self.query(left - 1)

    def __repr__(self) -> str:
        return f"FenwickTree({self.tree[1:]})"

