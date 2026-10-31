import numpy as np

class NeuralNetwork:
    def __init__(self, layers, lr=0.01):
        self.lr = lr
        self.weights = [np.random.randn(y, x) * 0.1 for x, y in zip(layers[:-1], layers[1:])]
        self.biases = [np.zeros((y, 1)) for y in layers[1:]]
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))