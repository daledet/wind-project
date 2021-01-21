import numpy as np
a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product)

# Same in Numpy

np_dot = np.dot(a, b)
print(np_dot)

# Same thing in Numpy with bias

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

outputs = np.dot(weights, inputs) + bias

print(outputs)

# With Biases

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]
layer_outputs = np.dot(weights, inputs) + biases

print(layer_outputs)

print(np.array([a]))
print(np.expand_dims(np.array(a), axis=0))

a = np.array([a])
b = np.array([b]).T
print(np.dot(a, b))

# Performing above on two matrices

inputs_matrix = [[1.0, 2.0, 3.0, 2.5],
                 [2.0, 5.0, -1.0, 2.0],
                 [-1.5, 2.7, 3.3, -0.8]]
weights_matrix = [[0.2, 0.8, -0.5, 1],
                  [0.5, -0.91, 0.26, -0.5],
                  [-0.26, -0.27, 0.17, 0.87]]
biases_matrix = [2.0, 3.0, 0.5]

layer_outputs_matrix = np.dot(
    inputs_matrix, np.array(weights_matrix).T) + biases_matrix
print(layer_outputs_matrix)
