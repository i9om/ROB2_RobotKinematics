from math import pi
from roboticstoolbox import DHRobot, RevoluteMDH
import numpy as np
from spatialmath import SE3

# Section 1 - Denavit-Hartenberg Parameters

# Homogeneous Transformation matrix for the base
T = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 352],
              [0, 0, 0, 1]])

# Define the links using Denavit-Hartenberg parameters
L = [
	RevoluteMDH(alpha =    0,        a=0,   d=0),
    RevoluteMDH(alpha = -90*pi/180,  a=70,  d=0,  offset=-90*pi/180),
    RevoluteMDH(alpha =     0,       a=360, d=0),
    RevoluteMDH(alpha=-90*pi/180,    a=0,   d=380),
    RevoluteMDH(alpha=90*pi/180,     a=0,   d=0),
    RevoluteMDH(alpha=-90*pi/180,    a=0,   d=0, ),
]

# Create the robot model
ABB140 = DHRobot(L, name='ABB')

# Define joint angles in radians
q = np.radians([10, 20, 30, 40, 50, 60])

# Forward kinematics to get the transformation matrix
T06 = ABB140.fkine(q)

# Extract Roll, Pitch, Yaw from T06 (ZYX convention)
RZYX = T06.rpy(order='zyx',unit='deg')

print("Rotation Angles (ZYX) for Section 1:", RZYX)

# Section 2 - Move base frame

TB0 = SE3([[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 352],
           [0, 0, 0, 1]])

# Compute TB6 by multiplying TB0 with T06
TB6 = TB0 * T06

# Extract Roll, Pitch, Yaw from TB6
RZYX = TB6.rpy(order='zyx', unit='deg')

print("Rotation Angles (ZYX) for Section 2:", RZYX)

# Section 3 - Move wrist frame

T6W = SE3([[-1, 0, 0, 0],
           [0, -1, 0, 0],
           [0, 0, 1, 65],
           [0, 0, 0, 1]])

# Compute TBW by multiplying TB0, T06, and T6W
TBW = TB0 * T06 * T6W
print(TBW)
# Extract Roll, Pitch, Yaw from TBW
ZYX = TBW.rpy(order="zyx", unit="deg")

print("Rotation Angles (ZYX) for Section 3:", ZYX)

# Section 4 - With Tool Data

TWT = SE3.Trans(-4, 0, 371.300) * SE3.Ry(45,unit='deg')

# Compute TBT by multiplying TB0, T06, T6W, and TWT
TBT = TB0 * T06 * T6W * TWT

# Extract Roll, Pitch, Yaw from TBT
ZYX = TBT.rpy(order='zyx', unit='deg')

print("Rotation Angles (ZYX) for Section 4:", ZYX)
print(TBT)
