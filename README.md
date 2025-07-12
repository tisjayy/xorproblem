# xorproblem
This project implements a simple neural network **from scratch using NumPy** to solve the classic **XOR problem** — a foundational example in understanding why neural networks need hidden layers and non-linear activation functions.

---

## 🧠 What is the XOR Problem?

The XOR (exclusive OR) logic gate outputs true (1) **only when the inputs differ**:

| Input 1 | Input 2 | XOR Output |
|---------|---------|------------|
|   0     |    0    |     0      |
|   0     |    1    |     1      |
|   1     |    0    |     1      |
|   1     |    1    |     0      |

This problem **cannot be solved by a simple linear model**, making it a great candidate to demonstrate the power of a neural network with a **hidden layer**.

---

## ⚙️ How It Works

- **Architecture**: 2 input neurons → 1 hidden layer (2 neurons, sigmoid) → 1 output neuron (sigmoid)
- **Forward Pass**: Calculates predictions based on current weights.
- **Backpropagation**: Calculates gradients of the error using the chain rule.
- **Gradient Descent**: Updates weights and biases to reduce prediction error.
- **Activation**: Sigmoid function for both hidden and output layers.

---

## 📦 Requirements

- Python 3.x
- NumPy
