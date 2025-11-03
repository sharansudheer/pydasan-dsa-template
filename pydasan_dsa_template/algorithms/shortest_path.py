import heapq

def dijkstra(graph, start):
    # graph: dict of node -> list of (neighbor, weight)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # priority queue (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

#test
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(dijkstra(graph, 'A'))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

"""
TODO

A) Polish This approach and all the Roaches using Raid Roach spray
B) Implement -

    1) bfs
    2) Bellman–Ford Algorithm
    3) Floyd–Warshall Algorithm
    4) Using NetworkX (built-in library)

Check on if it handles Negatives?

"""