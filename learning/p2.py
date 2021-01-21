# NN In Raw Python - Cleaner
inputs = [1, 2, 3, 2.5]


weights = [[0.2, 0.8, - 0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

layer_outputs = []
for neuron_weights, neruon_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neruon_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
