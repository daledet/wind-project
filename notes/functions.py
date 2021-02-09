import numpy as np


class LayerDense:  # Hidden Layers
    def __init__(self, n_inputs, n_neurons):
        # Ordered so that transpose is unnecessary
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class ActivationReLU:  # ReLU Object
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class ActivationSoftMax:  # Exponents and Normalize
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
