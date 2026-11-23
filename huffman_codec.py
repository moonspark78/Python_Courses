# huffman_codec.py
import heapq, struct, zlib
from collections import Counter
import heapq, struct, zlib
from collections import Counter
from itertools import count


def build_codes(freq):
    tie = count()
    heap = [(n, next(tie), {s: ""}) for s, n in sorted(freq.items())]
    heapq.heapify(heap)
    while len(heap) > 1:
        (n1, _, a), (n2, _, b) = heapq.heappop(heap), heapq.heappop(heap)
        merged = {s: "0" + c for s, c in a.items()} | {s: "1" + c for s, c in b.items()}
        heapq.heappush(heap, (n1 + n2, next(tie), merged))
    return {s: c or "0" for s, c in heap[0][2].items()} if heap else {}
