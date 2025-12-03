"""
Dijkstra's shortest path algorithm using a priority queue.
Graph format:
{
    "A": [("B", 5), ("C", 3)],
    ...
}
"""

from typing import Dict, List, Tuple
import heapq

Graph = Dict[str, List[Tuple[str, float]]]


def dijkstra(graph: Graph, start: str) -> Tuple[Dict[str, float], Dict[str, List[str]]]:
    """Compute shortest distances and paths from a start node."""
    
    dist = {node: float("inf") for node in graph}
    dist[start] = 0.0

    paths = {node: [] for node in graph}
    paths[start] = [start]

    pq: List[Tuple[float, str]] = [(0.0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, cost in graph[node]:
            new_dist = current_dist + cost

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                paths[neighbor] = paths[node] + [neighbor]
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, paths


if __name__ == "__main__":
    graph = {
        "A": [("B", 5), ("C", 3)],
        "B": [("A", 5), ("C", 1)],
        "C": [("A", 3), ("B", 1)]
    }
    d, p = dijkstra(graph, "A")
    print(d)
    print(p)
