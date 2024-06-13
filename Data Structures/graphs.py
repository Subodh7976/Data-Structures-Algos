from typing import Dict, List, Tuple, Any 


class Graph:
    def __init__(self) -> None:
        self._adjacency_list: Dict[Any, List[Any]] = {}
    
    def add_vertex(self, vertex: Any) -> None:
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = []
    
    def add_edge(self, vertex_1: Any, vertex_2: Any) -> None:
        if vertex_1 not in self._adjacency_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self._adjacency_list:
            self.add_vertex(vertex_2)
        self._adjacency_list[vertex_1].append(vertex_2)
        self._adjacency_list[vertex_2].append(vertex_1)
    
    def remove_vertex(self, vertex: Any) -> None:
        if vertex in self._adjacency_list:
            for adjacent in self._adjacency_list[vertex]:
                self._adjacency_list[adjacent].remove(vertex)
            del self._adjacency_list[vertex]
    
    def remove_edge(self, vertex_1: Any, vertex_2: Any) -> None:
        if vertex_1 in self._adjacency_list and vertex_2 in self._adjacency_list[vertex_1]:
            self._adjacency_list[vertex_1].remove(vertex_2)
        if vertex_2 in self._adjacency_list and vertex_1 in self._adjacency_list[vertex_2]:
            self._adjacency_list[vertex_2].remove(vertex_1)
    
    def get_vertices(self) -> List[Any]:
        return list(self._adjacency_list.keys())
    
    def get_edges(self) -> List[Tuple[Any, Any]]:
        edges = []
        for vertex, adjacents in self._adjacency_list.items():
            for adjacent in adjacents:
                if (adjacent, vertex) not in edges:
                    edges.append((vertex, adjacent))
        
        return edges 

    def bfs(self, start_index: Any) -> List[Any]:
        visited = set()
        queue = [start_index]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v in self._adjacency_list[vertex] 
                              if v not in visited])
        
        return result 
    
    def dfs(self, start_index: Any) -> List[Any]:
        visited = set()
        stack = [start_index]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend([v for v in self._adjacency_list[vertex] 
                              if v not in visited])
                
        return result
    
    def __repr__(self) -> str:
        return "\n".join(f"{vertex}: {adjacents}" for vertex, adjacents in self._adjacency_list.items())
    