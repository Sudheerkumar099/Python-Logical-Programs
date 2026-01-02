from collections import deque

graph = {
    "A":["B","C","E"],
    "B":["C","D"],
    "C":["D"],
    "D":["E"],
    "E":[]
}
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(graph,"A")
    
    