def bfs(start, end, graph) -> dict[str, str]:
    queue = [start]
    visited = {start: None}

    while queue:
        cur_node = queue.pop(0)
        if cur_node == end:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited # type: ignore


graph = {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['C', 'F'],
    'F': ['E'],
}

start = 'A'
end = 'E'
visited = bfs(start, end, graph)

way = []
cur_node = end
while cur_node != start:
    way.insert(0, cur_node)
    cur_node = visited[cur_node]

print(way)

