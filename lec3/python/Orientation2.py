
import numpy as np
from spatialmath import SO3, UnitQuaternion,SE3

# --------------------------------
# Given the Rotation matrix R
R = np.array([
    [0.9752, -0.0370,  0.2184],
    [0.0978,  0.9564, -0.2751],
    [-0.1987, 0.2896,  0.9363]
])

# --------------------------------
# 1. Compute Roll, Pitch, Yaw (RPY) corresponding to R
print('Exercise 21')

# Compute Pitch
Pitch = np.arctan2(-R[2, 0], np.sqrt(R[0, 0]**2 + R[1, 0]**2))

if abs(abs(Pitch) - np.pi / 2) < 0.00001:  # Check for gimbal lock
    Yaw = 0
    Roll = np.sign(Pitch) * np.arctan2(R[0, 1], R[1, 1])
else:
    Yaw = np.arctan2(R[1, 0] / np.cos(Pitch), R[0, 0] / np.cos(Pitch))
    Roll = np.arctan2(R[2, 1] / np.cos(Pitch), R[2, 2] / np.cos(Pitch))

print(f"Using matrices: Roll: {Roll}, Pitch: {Pitch}, Yaw: {Yaw}")

# Using the Robotics Toolbox
Rt = SO3([
    [0.9752, -0.0370,  0.2184],
    [0.0978,  0.9564, -0.2751],
    [-0.1987, 0.2896,  0.9363]
])

RPY = Rt.rpy(order='zyx')
print('Using the toolbox:',RPY)

# --------------------------------
# 2. Compute angle/axis representation

theta = np.arccos((np.trace(R) - 1) / 2)  # Trace of R gives the sum of diagonal elements

if abs(theta) < 0.000001:
    K = np.array([0, 0, 0])  # No rotation
else:
    K = 1 / (2 * np.sin(theta)) * np.array([
        R[2, 1] - R[1, 2],
        R[0, 2] - R[2, 0],
        R[1, 0] - R[0, 1]
    ])
print('-------------------------')
print('Exercise 22:')
print('Using matrices')
print(f"Angle (theta): {theta}")
print(f"Axis (K): {K}")

print('Using the toolbox')
thetat,Kt=Rt.angvec()
print(thetat,Kt)


# --------------------------------
# 3. Compute quaternions (Craig Eq 2.92)

e4 = 0.5 * np.sqrt(R[0, 0] + R[1, 1] + R[2, 2] + 1)
e1 = (R[2, 1] - R[1, 2]) / (4 * e4)
e2 = (R[0, 2] - R[2, 0]) / (4 * e4)
e3 = (R[1, 0] - R[0, 1]) / (4 * e4)

print('-------------------------')
print('Exercise 23:')
print('using matrices')
print(f"Quaternion: [{e4}, {e1}, {e2}, {e3}]")

# Using the Robotics Toolbox
print('using the toolbox')

q = Rt.UnitQuaternion()
print(f"Quaternion: {q}")
