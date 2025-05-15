from collections import deque

class Search:
    def __init__(self):
        self.graph=None

    def bfs(self,start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend([n for n in self.graph[node] if n not in visited])
        print(' ')

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
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

search=Search()
search.graph=graph
print('BFS')
search.bfs('A')
print('DFS')
search.dfs('A')
