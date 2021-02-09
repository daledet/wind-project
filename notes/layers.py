import numpy as np
from functions import *
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
# Inputs from wind => Average Windspeed, Standard Deviation
X = [[1.0, 2.0],
     [2.0, 5.0],
     [-1.5, 2.7]]


X, y = spiral_data(samples=100, classes=3)

dense1 = LayerDense(2, 3)
activation1 = ActivationReLU()

dense2 = LayerDense(3, 3)
activation2 = ActivationSoftMax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])
