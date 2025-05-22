from collections import deque

class SearchBase:
    def __init__(self):
        self.graph=None


    def Search(self):
        pass

class DFS(SearchBase):
    def __init__(self):
        super().__init__()

    def Search(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.Search(neighbor, visited)

class BFS(SearchBase):
    def __init__(self):
        super().__init__()

    def Search(self,start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend([n for n in self.graph[node] if n not in visited])
        print(' ')

# Example graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

bfs=BFS()
bfs.graph=graph
bfs.Search('A')

dfs=DFS()
dfs.graph=graph
dfs.Search('A')




