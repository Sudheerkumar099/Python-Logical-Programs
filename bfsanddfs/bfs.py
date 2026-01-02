from collections import deque

graph = {
    "A":["B","C","E"],
    "B":["C","D"],
    "C":["D"],
    "D":["E"],
    "E":["F"],
    "F":[]
}
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    queue.append(i)

bfs(graph,"A")
    
    