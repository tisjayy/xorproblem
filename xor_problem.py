# -*- coding: utf-8 -*-
"""xor problem.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12y_PBhYjWEwhLJGskwEfFSVTTnFMQIlr
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0,0],[0,1],[1,0],[1,1]])
d = np.array([0,1,1,0])

def initialize_network_parameters():
  inputSize = 2
  hiddenSize = 2
  outputSize = 1
  lr=0.1
  epochs= 18000

  w1 = np.random.rand(hiddenSize, inputSize)*2 - 1
  b1 = np.random.rand(hiddenSize, 1)*2 - 1
  w2 = np.random.rand(outputSize, hiddenSize)*2 - 1
  b2 = np.random.rand(outputSize, 1)*2 - 1

  return w1, b1, w2, b2, lr, epochs

# Get initialized parameters
w1, b1, w2, b2, lr, epochs = initialize_network_parameters()

# Training the network using backpropagation
error_list = []
for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(w1, X.T) + b1  # Weighted sum for hidden layer, transpose X
    a1 = 1 / (1 + np.exp(-z1))  # Sigmoid activation for hidden layer

    z2 = np.dot(w2, a1) + b2  # Weighted sum for output layer
    a2 = 1 / (1 + np.exp(-z2))  # Sigmoid activation for output layer

    # Error calculation and backpropagation
    error = d - a2  # Difference between expected and actual output
    da2 = error * (a2 * (1 - a2))  # Derivative for output layer
    dz2 = da2  # Gradient for output layer

    # Propagate error to hidden layer
    da1 = np.dot(w2.T, dz2)  # Gradient for hidden layer
    dz1 = da1 * (a1 * (1 - a1))  # Derivative for hidden layer

    # Update weights and biases
    w2 += lr * np.dot(dz2, a1.T)  # Update weights from hidden to output layer
    b2 += lr * np.sum(dz2, axis=1, keepdims=True)  # Update bias for output layer

    w1 += lr * np.dot(dz1, X)  # Update weights from input to hidden layer, use original X
    b1 += lr * np.sum(dz1, axis=1, keepdims=True)  # Update bias for hidden layer
    if (epoch+1)%10000 == 0:
        print("Epoch: %d, Average error: %0.05f"%(epoch, np.average(abs(error))))
        error_list.append(np.average(abs(error)))

# Testing the trained network
z1 = np.dot(w1, X.T) + b1  # Weighted sum for hidden layer, transpose X
a1 = 1 / (1 + np.exp(-z1))  # Sigmoid activation for hidden layer

z2 = np.dot(w2, a1) + b2  # Weighted sum for output layer
a2 = 1 / (1 + np.exp(-z2))  # Sigmoid activation for output layer

# Print results
print('Final output after training:', a2)
print('Ground truth', d)
print('Error after training:', d - a2) # Calculate the error using the actual output and ground truth
print('Average error: %0.05f'%np.average(abs(d - a2))) # Calculate average error using actual output and ground truth

# Plot error
plt.plot(error_list)
plt.title('Error')
plt.xlabel('Epochs')
plt.ylabel('Error')
plt.show()