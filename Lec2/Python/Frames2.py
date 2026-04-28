import numpy as np

# Define the matrices
UTA = np.array([
    [0.866, -0.5, 0, 11],
    [0.5, 0.866, 0.0, -1.0],
    [0.0, 0.0, 1.0, 8.0],
    [0, 0, 0, 1]
])

BTA = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.866, -0.5, 10.0],
    [0.0, 0.5, 0.866, 20.0],
    [0, 0, 0, 1]
])

CTU = np.array([
    [0.866, -0.5, 0.0, -3.0],
    [0.433, 0.75, -0.5, -3.0],
    [0.25, 0.433, 0.866, 3.0],
    [0, 0, 0, 1]
])

# Compute BTC
BTC = BTA @ np.linalg.inv(UTA) @ np.linalg.inv(CTU)

# Print result
print(np.round(BTC, 4))