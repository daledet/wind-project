import numpy as np

# Raw ReLU
inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
output = []

for i in inputs:
    output.append(max(0, i))

print(output)


class ActivationReLU:  # ReLU Object
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
