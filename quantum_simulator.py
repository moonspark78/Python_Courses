import cmath
import random

def quantum_state(n):
    state = [complex(random.random(), random.random()) for _ in range(n)]
    norm = sum(abs(x) ** 2 for x in state) ** 0.5
    return [x / norm for x in state]