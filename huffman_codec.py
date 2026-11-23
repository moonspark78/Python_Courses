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


def compress(data):
    codes = build_codes(freq := Counter(data))
    bits = "".join(codes[b] for b in data)
    bits += "0" * (-len(bits) % 8)
    table = b"".join(struct.pack(">BI", s, n) for s, n in sorted(freq.items()))
    return struct.pack(">IIH", zlib.crc32(data), len(data), len(freq)) + table + int(bits)

def decompress(blob):
    crc, size, k = struct.unpack_from(">IIH", blob)
    rev = {c: s for s, c in build_codes(dict(struct.unpack_from(">BI", blob, 10 + 5 * i) for i in range(k))).items()}
    out, cur = bytearray(), ""
    for bit in "".join(f"{b:08b}" for b in blob[10 + 5 * k:]):
        cur += bit
        if cur in rev and len(out) < size:
            out.append(rev[cur])
            cur = ""