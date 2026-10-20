import cmath
import random

def quantum_state(n):
    state = [complex(random.random(), random.random()) for _ in range(n)]
    norm = sum(abs(x) ** 2 for x in state) ** 0.5
    return [x / norm for x in state]

def evolve(state, steps):
    for _ in range(steps):
        phase = cmath.exp(1j * random.uniform(-3.14, 3.14))
        state = [x * phase for x in state]
        state = [x + complex(0, 0.01 * random.random()) for x in state]
        norm = sum(abs(x) ** 2 for x in state) ** 0.5