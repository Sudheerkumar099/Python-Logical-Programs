graph = {
    "A":["B","C","E"],
    "B":["C","D"],
    "C":["D"],
    "D":["E"],
    "E":["F"],
    "F":[]
}
def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph,n,visited)

dfs(graph,"A")