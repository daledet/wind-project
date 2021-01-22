import math
import numpy as np


layer_outputs = [4.8, 1.21, 2.385]
E = math.e

exp_values = []
for output in layer_outputs:
    exp_values.append(E ** output)
print('exponentiated values:')
print(exp_values)


norm_base = sum(exp_values)
norm_values = []
for value in exp_values:
    norm_values.append(value / norm_base)
print('Normalized exponentiated values:')
print(norm_values)
print('Sum of normalized values:', sum(norm_values))


# Using Numpy

# Values from the earlier previous when we described # what a neural network is
layer_outputs = [4.8, 1.21, 2.385]
# For each value in a vector, calculate the exponential value
exp_values = np.exp(layer_outputs)
print('exponentiated values:')
print(exp_values)
# Now normalize values
norm_values = exp_values / np.sum(exp_values)
print('normalized exponentiated values:')
print(norm_values)
print('sum of normalized values:', np.sum(norm_values))


layer_outputs = np.array([[4.8, 1.21, 2.385], [8.9, -1.81, 0.2],
                          [1.41, 1.051, 0.026]])
print(np.sum(layer_outputs))
print('Sum without axis')
print('This will be identical to the above since default is None:')
print(np.sum(layer_outputs, axis=None))
print(np.sum(layer_outputs, axis=0))

# Softmax activation


class Activation_Softmax:  # Forward pass
    def forward(self, inputs):
        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                            keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1,
                                            keepdims=True)

        self.output = probabilities


print(np.exp(1))
print(np.exp(10))
