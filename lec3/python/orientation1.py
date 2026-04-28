import numpy as np
from spatialmath import SO3, UnitQuaternion

# Solutions to Exercise 1 - Lecture: Orientations

# --------------------------------
# 1. Compute the rotation matrices which correspond to:
#    Extrinsic (fixed axis rotation) rotation about XYZ (Craig's roll, pitch, yaw):
#    Roll(X)=30; Pitch(Y)=50, Yaw(Z)=-20

roll = np.radians(30)
pitch = np.radians(50)
yaw = np.radians(-20)
# Method 1: Using elementary rotations and the product of these
R1_multi = SO3.Rz(yaw) * SO3.Ry(pitch) * SO3.Rx(roll)

# Method 2: Using matrix computations
R1_matrix = np.array([
    [np.cos(yaw) * np.cos(pitch), np.cos(yaw) * np.sin(pitch) * np.sin(roll) - np.sin(yaw) * np.cos(roll), np.cos(yaw) * np.sin(pitch) * np.cos(roll) + np.sin(yaw) * np.sin(roll)],
    [np.sin(yaw) * np.cos(pitch), np.sin(yaw) * np.sin(pitch) * np.sin(roll) + np.cos(yaw) * np.cos(roll), np.sin(yaw) * np.sin(pitch) * np.cos(roll) - np.cos(yaw) * np.sin(roll)],
    [-np.sin(pitch), np.cos(pitch) * np.sin(roll), np.cos(pitch) * np.cos(roll)]
])

# Method 3: Using the Robotics Toolbox
R1_toolbox = SO3.RPY([roll, pitch, yaw], order='zyx')

print('Exercise11:')
print('Method 1: Using elementary rotations and the product of these\n',R1_multi)
print('Method 2: Using matrix computations\n',R1_matrix)
print('Method 3: Using the toolbox\n',R1_toolbox)
# --------------------------------
# Compute the rotation matrices which correspond to:
#    Intrinsic rotation about ZYX
#    X(gamma)=20; Y(beta)=-15, Z(alpha)=30

alpha = np.radians(30)
beta = np.radians(-15)
gamma = np.radians(20)

# Method 1: Using elementary rotations and the product of these
R2_multi = SO3.Rz(alpha) * SO3.Ry(beta) * SO3.Rx(gamma)

# Method 2: Using Using matrix computations
R2_matrix = np.array([
    [np.cos(alpha) * np.cos(beta), np.cos(alpha) * np.sin(beta) * np.sin(gamma) - np.sin(alpha) * np.cos(gamma),
     np.cos(alpha) * np.sin(beta) * np.cos(gamma) + np.sin(alpha) * np.sin(gamma)],
    [np.sin(alpha) * np.cos(beta), np.sin(alpha) * np.sin(beta) * np.sin(gamma) + np.cos(alpha) * np.cos(gamma),
     np.sin(alpha) * np.sin(beta) * np.cos(gamma) - np.cos(alpha) * np.sin(gamma)],
    [-np.sin(beta), np.cos(beta) * np.sin(gamma), np.cos(beta) * np.cos(gamma)]
])

# Method 3: Using the Robotics Toolbox
R2_toolbox = SO3.RPY([gamma, beta, alpha], order='zyx')

print('-----------------------------------------')
print('Exercise12:')
print('Method 1: Using elementary rotations and the product of these\n',R2_multi)
print('Method 2: Using matrix computations\n',R2_matrix)
print('Method 3: Using the toolbox\n',R2_toolbox)
# --------------------------------
# Compute the rotation matrices which correspond to:
#    Angle/axis representation: theta = 21.8583 degrees; k = [0.3379, 0.4808, 0.8093]


theta = np.radians(21.8583)
k = np.array([0.3379, 0.4808, 0.8093])

# Method 1: Using the axis/angle formula
kx, ky, kz = k
R3_matrix = np.array([
    [kx * kx * (1 - np.cos(theta)) + np.cos(theta), kx * ky * (1 - np.cos(theta)) - kz * np.sin(theta),
     kx * kz * (1 - np.cos(theta)) + ky * np.sin(theta)],
    [kx * ky * (1 - np.cos(theta)) + kz * np.sin(theta), ky * ky * (1 - np.cos(theta)) + np.cos(theta),
     ky * kz * (1 - np.cos(theta)) - kx * np.sin(theta)],
    [kx * kz * (1 - np.cos(theta)) - ky * np.sin(theta), kz * ky * (1 - np.cos(theta)) + kx * np.sin(theta),
     kz * kz * (1 - np.cos(theta)) + np.cos(theta)]
])

# Method2: Using the Robotics Toolbox
R3_toolbox = SO3.AngleAxis(theta, k)

print('-----------------------------------------')
print('Exercise13:')
print('Method 1: Using the axis/angle formulas\n',R3_matrix)
print('Method 2: Using the toolbox\n',R3_toolbox)
# --------------------------------
# Compute the rotation matrices which correspond to:
#    Quaternion = [0.064071, 0.091158, 0.15344, 0.98186]

e1, e2, e3, e4 = 0.064071, 0.091158, 0.15344, 0.98186

# Method 1: Using quaternion to matrix formula
R4_matrix = np.array([
    [1 - 2 * e2**2 - 2 * e3**2, 2 * (e1 * e2 - e3 * e4), 2 * (e1 * e3 + e2 * e4)],
    [2 * (e1 * e2 + e3 * e4), 1 - 2 * e1**2 - 2 * e3**2, 2 * (e2 * e3 - e1 * e4)],
    [2 * (e1 * e3 - e2 * e4), 2 * (e2 * e3 + e1 * e4), 1 - 2 * e1**2 - 2 * e2**2]
])

# Method 2: Compute axis/angle from quaternion
theta = 2 * np.arccos(e4)
sin_half_theta = np.sqrt(1 - e4**2)
kx, ky, kz = e1 / sin_half_theta, e2 / sin_half_theta, e3 / sin_half_theta

R4_axisAngle = np.array([
    [kx * kx * (1 - np.cos(theta)) + np.cos(theta), kx * ky * (1 - np.cos(theta)) - kz * np.sin(theta),
     kx * kz * (1 - np.cos(theta)) + ky * np.sin(theta)],
    [kx * ky * (1 - np.cos(theta)) + kz * np.sin(theta), ky * ky * (1 - np.cos(theta)) + np.cos(theta),
     ky * kz * (1 - np.cos(theta)) - kx * np.sin(theta)],
    [kx * kz * (1 - np.cos(theta)) - ky * np.sin(theta), kz * ky * (1 - np.cos(theta)) + kx * np.sin(theta),
     kz * kz * (1 - np.cos(theta)) + np.cos(theta)]
])

# Method 3: Using the Robotics Toolbox
q= UnitQuaternion([e4, e1, e2, e3])
R4_toolbox = q.R

print('-----------------------------------------')
print('Exercise14:')
print('Method 1: Using quaternion to matrix formula\n',R4_matrix)
print('Method 2: Compute axis/angle from quaternion\n',R4_axisAngle)
print('Method 3: Using the toolbox\n',R4_toolbox)
