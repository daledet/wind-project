import numpy as np


layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]


class ActivationReLU:  # ReLU Object
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class ActivationSoftMax:  # Exponents and Normalize
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
