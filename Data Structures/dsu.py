class DisjointSetUnion:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u: int) -> int:
        """
        Finds the representative of the set that u belongs to.
        Implements path compression to keep the tree flat.
        
        Parameters:
        u (int): The element to find the set representative for.
        
        Returns:
        int: The representative of the set containing u.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        """
        Unites the sets that u and v belong to.
        Implements union by rank to keep the tree balanced.
        
        Parameters:
        u (int): The first element.
        v (int): The second element.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

    def __repr__(self) -> str:
        return f"DisjointSetUnion(parent={self.parent}, rank={self.rank})"

