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