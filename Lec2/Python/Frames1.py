import numpy as np

# Define the matrices
ARB = np.array([
    [0.7052, -0.3749, 0.6018],
    [0.5546, 0.8205, -0.1387],
    [-0.4418, 0.4316, 0.7865]
])

ATB = np.array([
    [0.7052, -0.3749, 0.6018, 646.9],
    [0.5546, 0.8205, -0.1387, 103.8],
    [-0.4418, 0.4316, 0.7865, -329.7],
    [0, 0, 0, 1]
])

# Exercise 1.1
AV1 = np.array([2, 5, 7])
AP1 = np.array([53, 15, -35, 1])

# Compute results
BV1 = np.linalg.inv(ARB) @ AV1
BP1 = np.linalg.inv(ATB) @ AP1

print("Exercise 1.1:")
print("BV1 =", np.round(BV1, 4))
print("BP1 =", np.round(BP1, 4))

# Exercise 1.2
AV1 = np.array([2, 5, 7])
AP1 = np.array([10, -40, 25, 1])

# Compute results
BV1 = np.linalg.inv(ARB) @ AV1
BP1 = np.linalg.inv(ATB) @ AP1

print("\nExercise 1.2:")
print("BV1 =", np.round(BV1, 4))
print("BP1 =", np.round(BP1, 4))