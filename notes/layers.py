import numpy as np
from functions import ActivationReLU

np.random.seed(0)

# Inputs from wind => Average Windspeed, Standard Deviation
X = [[1.0, 2.0],
     [2.0, 5.0],
     [-1.5, 2.7]]


class LayerDense:  # Hidden Layers
    def __init__(self, n_inputs, n_neurons):
        # Ordered so that transpose is unnecessary
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


# Hidden Layer 1
layer1 = LayerDense(2, 5)
activation1 = ActivationReLU()

layer1.forward(X)
activation1.forward(layer1.output)

print(activation1.output)
