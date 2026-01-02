def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        count += 1
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            for sibling in graph[node]:
                if sibling not in visited:
                    queue.append(sibling)


graph = {
    'A': ['B', 'C',"E"],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    "E": ["F"],
    "F": []
}
bfs(graph, 'A')
    