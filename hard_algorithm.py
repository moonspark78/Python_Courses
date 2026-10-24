# hard_algorithm.py
import heapq
from collections import defaultdict


def shortest_paths(graph, start):
    distances = defaultdict(lambda: float("inf"))
    previous = {}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        distance, node = heapq.heappop(queue)
        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                heapq.heappush(queue, (new_distance, neighbor))

    return dict(distances), previous

def reconstruct_path(previous, target):
    path = []
    while target in previous:
        path.append(target)
        target = previous[target]
    path.append(target)
    return path[::-1]