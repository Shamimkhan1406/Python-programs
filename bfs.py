from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start = 'A'
goal = 'F'
shortest_path = bfs_shortest_path(graph, start, goal)
print("Shortest path from {} to {}: {}".format(start, goal, shortest_path))
