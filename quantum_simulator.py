import cmath
import random

def quantum_state(n):
    state = [complex(random.random(), random.random()) for _ in range(n)]