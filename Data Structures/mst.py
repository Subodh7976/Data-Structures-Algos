from typing import List, Tuple

class DisjointSetUnion:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
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

class KruskalMST:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, u: int, v: int, weight: int) -> None:
        self.edges.append((weight, u, v))

    def find_mst(self) -> List[Tuple[int, int, int]]:
        self.edges.sort()  # Sort edges by weight
        dsu = DisjointSetUnion(self.num_vertices)
        mst = []

        for weight, u, v in self.edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
                mst.append((u, v, weight))

        return mst

    def __repr__(self) -> str:
        return f"KruskalMST(num_vertices={self.num_vertices}, edges={self.edges})"


