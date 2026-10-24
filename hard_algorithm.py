# hard_algorithm.py
import heapq
from collections import defaultdict


def shortest_paths(graph, start):
    distances = defaultdict(lambda: float("inf"))